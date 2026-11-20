/* Hairline 行为脚本：一个文件，不依赖任何库。靠标记上的属性接管行为，不加载它时组件照样能看。 */
(function () {
  'use strict';
  var doc = document;
  var G = { version: '1.0.0' };
  var FOCUSABLE = 'a[href], button:not([disabled]), input:not([disabled]):not([type="hidden"]), select:not([disabled]), textarea:not([disabled]), summary, [tabindex]:not([tabindex="-1"])';

  function $$(sel, root) { return Array.prototype.slice.call((root || doc).querySelectorAll(sel)); }
  function emit(el, name, detail) { el.dispatchEvent(new CustomEvent(name, { bubbles: true, detail: detail })); }
  function visible(el) { return !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length); }
  function focusables(root) { return $$(FOCUSABLE, root).filter(visible); }
  function isEn(el) { var l = el.closest('[lang]'); return !!l && /^en/i.test(l.getAttribute('lang')); }
  function replay(el, cls) { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); }
  var uid = 0;
  function id(el, prefix) { if (!el.id) { uid += 1; el.id = (prefix || 'hao') + '-' + uid; } return el.id; }

  /* ---------- 弹窗与底部弹层 ---------- */
  var modals = [], locked = null;
  /* 真的模态层打开时，后面的页面不跟着滚；滚动条让出的宽度用内边距补上，页面不会横跳。 */
  function scrollLock() {
    var need = modals.some(function (m) { return m.scrim.hasAttribute('data-hao-modal'); });
    var root = doc.documentElement;
    if (need && !locked) {
      var gap = window.innerWidth - root.clientWidth;
      locked = { overflow: root.style.overflow, paddingRight: root.style.paddingRight };
      root.style.overflow = 'hidden';
      if (gap > 0) root.style.paddingRight = gap + 'px';
    } else if (!need && locked) {
      root.style.overflow = locked.overflow;
      root.style.paddingRight = locked.paddingRight;
      locked = null;
    }
  }
  function modalOpen(scrim, opener) {
    if (!scrim || !scrim.hidden) return;
    var panel = scrim.querySelector('.hao-dialog, .hao-sheet') || scrim;
    var inerted = [];
    var node = scrim;
    while (node && node !== doc.body) {
      Array.prototype.forEach.call(node.parentNode.children, function (sib) {
        if (sib !== node && !sib.inert && sib.tagName !== 'SCRIPT') { sib.inert = true; inerted.push(sib); }
      });
      node = node.parentNode;
    }
    scrim.hidden = false;
    replay(scrim, 'hao-scrim--enter');
    if (panel.classList.contains('hao-sheet')) replay(panel, 'hao-sheet--enter');
    if (panel.classList.contains('hao-dialog')) replay(panel, 'hao-dialog--enter');
    modals.push({ scrim: scrim, panel: panel, opener: opener || doc.activeElement, inerted: inerted });
    scrollLock();
    var first = panel.querySelector('[data-hao-initial]') || focusables(panel)[0];
    if (first) first.focus(); else { panel.tabIndex = -1; panel.focus(); }
    emit(scrim, 'hao-open');
  }
  function modalClose(scrim) {
    var i = modals.length - 1;
    if (scrim) { for (i = modals.length - 1; i >= 0; i -= 1) if (modals[i].scrim === scrim) break; }
    if (i < 0) return;
    var m = modals.splice(i, 1)[0];
    m.scrim.hidden = true;
    m.inerted.forEach(function (el) { el.inert = false; });
    scrollLock();
    if (m.opener && m.opener.focus) m.opener.focus();
    emit(m.scrim, 'hao-close');
  }
  G.dialog = { open: modalOpen, close: modalClose };

  /* ---------- 菜单 ---------- */
  var menuNow = null;
  function menuItems(menu) { return $$('[role="menuitem"]', menu).filter(visible); }
  function menuOpen(menu, trigger) {
    if (menuNow) menuClose(false);
    menu.hidden = false;
    menu.classList.add('hao-menu--float');
    var r = trigger.getBoundingClientRect(), mw = menu.offsetWidth, mh = menu.offsetHeight;
    var left = Math.min(Math.max(8, r.left), window.innerWidth - mw - 8);
    var top = r.bottom + 6;
    var up = top + mh > window.innerHeight - 8 && r.top - mh - 6 > 8;
    if (up) top = r.top - mh - 6;
    menu.style.left = left + 'px';
    menu.style.top = top + 'px';
    /* 卷帘：朝哪边放下来，跟着菜单在按钮的上面还是下面 */
    menu.classList.toggle('hao-menu--up', up);
    replay(menu, 'hao-menu--enter');
    trigger.setAttribute('aria-expanded', 'true');
    menuNow = { menu: menu, trigger: trigger };
    var items = menuItems(menu);
    if (items[0]) items[0].focus();
  }
  function menuClose(refocus) {
    if (!menuNow) return;
    var m = menuNow; menuNow = null;
    m.menu.hidden = true;
    m.menu.classList.remove('hao-menu--enter', 'hao-menu--up', 'hao-menu--float');
    m.trigger.setAttribute('aria-expanded', 'false');
    if (refocus !== false) m.trigger.focus();
  }
  G.menu = { open: menuOpen, close: menuClose };

  /* ---------- 标签页 ---------- */
  function tabSelect(tab, focus) {
    var list = tab.closest('[role="tablist"]');
    if (!list) return;
    $$('[role="tab"]', list).forEach(function (t) {
      var on = t === tab;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      var panel = t.getAttribute('aria-controls') && doc.getElementById(t.getAttribute('aria-controls'));
      if (panel) panel.hidden = !on;
    });
    if (focus) tab.focus();
    emit(tab, 'hao-change', { tab: tab });
  }

  /* ---------- 轻提示 ---------- */
  var toastQueue = [], toastBusy = false, toastRegion = null;
  function toastNext() {
    if (toastBusy || !toastQueue.length) return;
    toastBusy = true;
    var job = toastQueue.shift();
    if (!toastRegion) {
      toastRegion = doc.createElement('div');
      toastRegion.className = 'hao-toast-region';
      toastRegion.setAttribute('role', 'status');
      toastRegion.setAttribute('aria-live', 'polite');
      doc.body.appendChild(toastRegion);
    }
    var el = doc.createElement('div');
    el.className = 'hao-toast hao-toast--enter';
    if (job.opts.lang) el.lang = job.opts.lang;
    if (job.opts.ok) { var ok = doc.createElement('span'); ok.className = 'hao-toast__ok'; ok.setAttribute('aria-hidden', 'true'); el.appendChild(ok); }
    el.appendChild(doc.createTextNode(job.text));
    var timer = null;
    function done() { clearTimeout(timer); if (el.parentNode) el.parentNode.removeChild(el); toastBusy = false; toastNext(); }
    if (job.opts.action) {
      var b = doc.createElement('button');
      b.className = 'hao-toast__action'; b.type = 'button'; b.textContent = job.opts.action;
      b.addEventListener('click', function () { if (job.opts.onAction) job.opts.onAction(); done(); });
      el.appendChild(b);
    }
    var ms = job.opts.duration || (job.opts.action ? 8000 : 4000);
    function arm() { clearTimeout(timer); timer = setTimeout(done, ms); }
    el.addEventListener('mouseenter', function () { clearTimeout(timer); });
    el.addEventListener('mouseleave', arm);
    el.addEventListener('focusin', function () { clearTimeout(timer); });
    el.addEventListener('focusout', arm);
    toastRegion.appendChild(el);
    arm();
  }
  G.toast = function (text, opts) { toastQueue.push({ text: text, opts: opts || {} }); toastNext(); };

  /* ---------- 气泡提示 ---------- */
  var tipNow = null, tipTimer = null, tipLeave = null;
  function tipShow(target) {
    tipHide();
    var tip = doc.createElement('span');
    tip.className = 'hao-tip hao-tip--float'; tip.setAttribute('role', 'tooltip');
    tip.textContent = target.getAttribute('data-hao-tip');
    var l = target.closest('[lang]'); if (l) tip.lang = l.getAttribute('lang');
    doc.body.appendChild(tip);
    var r = target.getBoundingClientRect(), w = tip.offsetWidth, h = tip.offsetHeight;
    var top = r.top - h - 8; if (top < 8) top = r.bottom + 8;
    tip.style.left = Math.min(Math.max(8, r.left + r.width / 2 - w / 2), window.innerWidth - w - 8) + 'px';
    tip.style.top = top + 'px';
    target.setAttribute('aria-describedby', id(tip, 'hao-tip'));
    tipNow = { tip: tip, target: target };
  }
  /* 鼠标从元素移到提示上要跨过一道缝，所以晚一点收，移到提示上就不收。 */
  function tipHideSoon() { clearTimeout(tipLeave); tipLeave = setTimeout(tipHide, 120); }
  function tipHide() {
    clearTimeout(tipTimer); clearTimeout(tipLeave);
    if (!tipNow) return;
    tipNow.target.removeAttribute('aria-describedby');
    if (tipNow.tip.parentNode) tipNow.tip.parentNode.removeChild(tipNow.tip);
    tipNow = null;
  }

  /* ---------- 步进器 ---------- */
  function stepperApply(st, value) {
    var out = st.querySelector('output'), btns = $$('button', st);
    var min = parseFloat(st.getAttribute('data-min')), max = parseFloat(st.getAttribute('data-max'));
    if (!isNaN(min)) value = Math.max(min, value);
    if (!isNaN(max)) value = Math.min(max, value);
    out.textContent = String(value);
    out.value = String(value);
    if (btns[0]) btns[0].disabled = !isNaN(min) && value <= min;
    if (btns[1]) btns[1].disabled = !isNaN(max) && value >= max;
    return value;
  }
  function stepperStep(st, dir) {
    var out = st.querySelector('output');
    var step = parseFloat(st.getAttribute('data-step')) || 1;
    var before = parseFloat(out.textContent) || 0;
    var after = stepperApply(st, before + dir * step);
    if (after !== before) emit(st, 'hao-change', { value: after });
    return after !== before;
  }
  var holdTimer = null, holdRepeat = null, held = false;
  function holdStop() { clearTimeout(holdTimer); clearInterval(holdRepeat); holdTimer = holdRepeat = null; }

  /* ---------- 评分 ---------- */
  function rateSet(group, btn, focus) {
    var btns = $$('[role="radio"]', group), n = btns.indexOf(btn);
    btns.forEach(function (b, i) {
      b.setAttribute('aria-checked', i === n ? 'true' : 'false');
      b.tabIndex = i === n ? 0 : -1;
      var plum = b.querySelector('.hao-plum');
      if (plum) plum.classList.toggle('hao-plum--on', i <= n);
      $$('circle.on', b).forEach(function (c) { c.classList.remove('on'); });
    });
    if (focus) btn.focus();
    emit(group, 'hao-change', { value: n + 1 });
  }

  /* ---------- 列表里的单选 ---------- */
  function listOptions(list) { return $$('[role="option"]', list).filter(function (o) { return !o.disabled; }); }
  function listSelect(list, opt, focus) {
    var opts = $$('[role="option"]', list), check = list.querySelector('.hao-list__check');
    opts.forEach(function (o) {
      var on = o === opt;
      o.setAttribute('aria-selected', on ? 'true' : 'false');
      o.tabIndex = on ? 0 : -1;
    });
    if (!check) { check = doc.createElement('span'); check.className = 'hao-list__check'; check.setAttribute('aria-hidden', 'true'); }
    opt.appendChild(check);
    if (focus) opt.focus();
    emit(list, 'hao-change', { value: opts.indexOf(opt), option: opt });
  }

  /* ---------- 全选 ---------- */
  function checkallSync(master) {
    var boxes = $$('input[type="checkbox"][name="' + master.getAttribute('data-hao-checkall') + '"]:not([disabled])');
    var on = boxes.filter(function (b) { return b.checked; }).length;
    master.checked = boxes.length > 0 && on === boxes.length;
    master.indeterminate = on > 0 && on < boxes.length;
  }

  /* ---------- 字数 ---------- */
  function countSync(input) {
    var field = input.closest('.hao-field'), out = field && field.querySelector('.hao-field__count');
    if (!out) return;
    var max = input.getAttribute('maxlength');
    out.textContent = max ? input.value.length + ' / ' + max : String(input.value.length);
  }

  /* ---------- 日历 ---------- */
  var ZH_MONTH = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'];
  var ZH_NUM = '一二三四五六七八九十';
  var TERMS = [
    ['小寒', 'Minor Cold', 5.4055], ['大寒', 'Major Cold', 20.12], ['立春', 'Start of Spring', 3.87], ['雨水', 'Rain Water', 18.73],
    ['惊蛰', 'Awakening of Insects', 5.63], ['春分', 'Spring Equinox', 20.646], ['清明', 'Clear and Bright', 4.81], ['谷雨', 'Grain Rain', 20.1],
    ['立夏', 'Start of Summer', 5.52], ['小满', 'Grain Buds', 21.04], ['芒种', 'Grain in Ear', 5.678], ['夏至', 'Summer Solstice', 21.37],
    ['小暑', 'Minor Heat', 7.108], ['大暑', 'Major Heat', 22.83], ['立秋', 'Start of Autumn', 7.5], ['处暑', 'End of Heat', 23.13],
    ['白露', 'White Dew', 7.646], ['秋分', 'Autumn Equinox', 23.042], ['寒露', 'Cold Dew', 8.318], ['霜降', 'Frost Descent', 23.438],
    ['立冬', 'Start of Winter', 7.438], ['小雪', 'Minor Snow', 22.36], ['大雪', 'Major Snow', 7.18], ['冬至', 'Winter Solstice', 21.94]
  ];
  var lunarFmt = null;
  try { lunarFmt = new Intl.DateTimeFormat('zh-CN-u-ca-chinese', { year: 'numeric', month: 'long', day: 'numeric' }); if (!/chinese/.test(lunarFmt.resolvedOptions().calendar)) lunarFmt = null; } catch (e) { lunarFmt = null; }
  function lunarDayName(n) {
    if (n === 10) return '初十'; if (n === 20) return '二十'; if (n === 30) return '三十';
    return ['初', '十', '廿', '三'][Math.floor((n - 1) / 10)] + ZH_NUM.charAt((n - 1) % 10);
  }
  function lunar(date) {
    if (G.calendar && G.calendar.source) return G.calendar.source(date);
    if (!lunarFmt) return null;
    var o = {};
    lunarFmt.formatToParts(date).forEach(function (p) { o[p.type] = p.value; });
    var day = parseInt(o.day, 10);
    if (!day) return null;
    var bare = o.month.replace('闰', '');
    var mn = { '正月': 1, '冬月': 11, '腊月': 12 }[bare] || (ZH_MONTH.indexOf(bare) + 1);
    return { year: o.yearName || '', month: o.month, monthNumber: mn, leap: /闰/.test(o.month), day: day, name: lunarDayName(day) };
  }
  /* 节气：二十一世纪通用的近似算式，个别年份会差一天。要准确，用 G.calendar.terms 换成历算数据。 */
  function termsOf(year, month) {
    if (year < 2001 || year > 2100) return {};
    var y = year % 100 || 100, out = {};
    [month * 2, month * 2 + 1].forEach(function (i) {
      var t = TERMS[i];
      var leap = Math.floor((month < 2 ? y - 1 : y) / 4);
      out[Math.floor(y * 0.2422 + t[2]) - leap] = { zh: t[0], en: t[1] };
    });
    return out;
  }
  function sameDay(a, b) { return !!a && !!b && a.getFullYear() === b.getFullYear() && a.getMonth() === b.getMonth() && a.getDate() === b.getDate(); }
  function parseDate(s) { var m = /^(\d{4})-(\d{1,2})-(\d{1,2})$/.exec(s || ''); return m ? new Date(+m[1], +m[2] - 1, +m[3], 12) : null; }
  function iso(d) { return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
  function el(tag, cls, text) { var n = doc.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; }
  function icon(name) { var i = el('i', 'hao-icon hao-icon--' + name); i.setAttribute('aria-hidden', 'true'); return i; }

  function calendarCreate(root) {
    if (root.haoCalendar) return root.haoCalendar;
    var en = isEn(root);
    var mode = root.getAttribute('data-mode') || 'plain';
    if (!lunarFmt && mode !== 'plain') mode = 'plain';
    if (en && mode === 'lunar') mode = 'moon';
    var today = parseDate(root.getAttribute('data-today')) || new Date();
    today.setHours(12, 0, 0, 0);
    var selected = parseDate(root.getAttribute('data-value'));
    var view = new Date((selected || today).getFullYear(), (selected || today).getMonth(), 1, 12);
    var focusDate = new Date((selected || today).getTime());
    var termFn = function (y, m) { return (G.calendar.terms || termsOf)(y, m); };

    function render(keepFocus) {
      var y = view.getFullYear(), m = view.getMonth();
      var terms = root.getAttribute('data-terms') === 'off' ? {} : termFn(y, m);
      root.textContent = '';
      var head = el('div', 'hao-cal__head');
      var monthName = en ? new Intl.DateTimeFormat('en', { month: 'long' }).format(view) : ZH_MONTH[m];
      var title = el('h2', 'hao-cal__title', y === today.getFullYear() ? monthName : (en ? monthName + ' ' + y : y + ' 年' + monthName));
      title.id = id(root, 'hao-cal') + '-title';
      title.setAttribute('aria-live', 'polite');
      var nav = el('span');
      var prev = el('button', 'hao-cal__nav'); prev.type = 'button'; prev.setAttribute('aria-label', en ? 'Previous month' : '上个月'); prev.appendChild(icon('chevron-left'));
      var next = el('button', 'hao-cal__nav'); next.type = 'button'; next.setAttribute('aria-label', en ? 'Next month' : '下个月'); next.appendChild(icon('chevron-right'));
      prev.addEventListener('click', function () { shift(-1, true); });
      next.addEventListener('click', function () { shift(1, true); });
      nav.appendChild(prev); nav.appendChild(next);
      head.appendChild(title); head.appendChild(nav);
      root.appendChild(head);

      /* 读屏要的是「表格、行、格」三层：一行星期，然后一周一行。 */
      var grid = el('div', 'hao-cal__grid'); grid.setAttribute('role', 'grid'); grid.setAttribute('aria-labelledby', title.id);
      var row = el('div', 'hao-cal__row'); row.setAttribute('role', 'row');
      var dowFull = en ? ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] : ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'];
      (en ? ['M', 'T', 'W', 'T', 'F', 'S', 'S'] : ['一', '二', '三', '四', '五', '六', '日']).forEach(function (d, n) {
        var h = el('span', 'hao-cal__dow', d); h.setAttribute('role', 'columnheader'); h.setAttribute('aria-label', dowFull[n]);
        row.appendChild(h);
      });
      grid.appendChild(row);
      var start = new Date(y, m, 1, 12);
      start.setDate(1 - ((start.getDay() + 6) % 7));
      var weeks = Math.ceil((((new Date(y, m, 1).getDay() + 6) % 7) + new Date(y, m + 1, 0).getDate()) / 7);
      var toFocus = null;
      for (var i = 0; i < weeks * 7; i += 1) {
        if (i % 7 === 0) { row = el('div', 'hao-cal__row'); row.setAttribute('role', 'row'); grid.appendChild(row); }
        var d = new Date(start.getFullYear(), start.getMonth(), start.getDate() + i, 12);
        var out = d.getMonth() !== m;
        var b = el('button', 'hao-cal__day' + (out ? ' hao-cal__day--out' : ''));
        b.type = 'button';
        b.setAttribute('data-date', iso(d));
        b.appendChild(doc.createTextNode(String(d.getDate())));
        var lu = mode !== 'plain' ? lunar(d) : null;
        var term = !out && terms[d.getDate()];
        var label = new Intl.DateTimeFormat(en ? 'en' : 'zh-CN', { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' }).format(d);
        if (mode === 'lunar' && lu) {
          var sm = el('small', term ? '' : (lu.day === 1 ? 'hao-cal__lunar hao-cal__lunar--first' : 'hao-cal__lunar'), term ? term.zh : (lu.day === 1 ? lu.month : lu.name));
          b.appendChild(sm);
          label += '，农历' + lu.month + lu.name + (term ? '，' + term.zh : '');
        } else if (mode === 'moon' && lu) {
          var moon = el('i', 'hao-moon hao-moon--xs' + (lu.day > 15 ? ' hao-moon--wane' : ''));
          moon.style.setProperty('--p', ((1 - Math.cos(2 * Math.PI * (lu.day - 1) / 29.53)) / 2).toFixed(2));
          b.appendChild(moon);
          if (term) label += en ? ', ' + term.en : '，' + term.zh;
        } else if (term) {
          b.appendChild(en ? el('small', 'hao-cal__dot') : el('small', '', term.zh));
          label += en ? ', ' + term.en : '，' + term.zh;
        }
        b.setAttribute('aria-label', label);
        if (sameDay(d, today)) b.setAttribute('aria-current', 'date');
        b.setAttribute('aria-pressed', sameDay(d, selected) ? 'true' : 'false');
        b.tabIndex = -1;
        if (sameDay(d, focusDate)) toFocus = b;
        var cell = el('div', 'hao-cal__cell'); cell.setAttribute('role', 'gridcell');
        if (sameDay(d, selected)) cell.setAttribute('aria-selected', 'true');
        cell.appendChild(b);
        row.appendChild(cell);
      }
      if (!toFocus) toFocus = grid.querySelector('.hao-cal__day:not(.hao-cal__day--out)');
      toFocus.tabIndex = 0;
      root.appendChild(grid);

      var foot = el('p', 'hao-cal__foot');
      var tl = mode !== 'plain' ? lunar(today) : null;
      if (tl) foot.appendChild(el('span', '', en ? 'Today: lunar month ' + (tl.monthNumber || '') + (tl.leap ? ' (leap)' : '') + ', day ' + tl.day : '今天 ' + tl.year + '年' + tl.month + tl.name));
      if (mode !== 'lunar') {
        Object.keys(terms).forEach(function (day) {
          var s = el('span'); s.appendChild(el('i'));
          s.appendChild(doc.createTextNode(en ? new Intl.DateTimeFormat('en', { month: 'short' }).format(view) + ' ' + day + ', ' + terms[day].en : day + ' 日' + terms[day].zh));
          foot.appendChild(s);
        });
      }
      if (foot.childNodes.length) root.appendChild(foot);
      if (keepFocus === 'day') toFocus.focus();
    }
    function shift(n, fromNav) {
      view = new Date(view.getFullYear(), view.getMonth() + n, 1, 12);
      var last = new Date(view.getFullYear(), view.getMonth() + 1, 0).getDate();
      focusDate = new Date(view.getFullYear(), view.getMonth(), Math.min(focusDate.getDate(), last), 12);
      render(fromNav ? null : 'day');
      if (fromNav) { var btn = $$('.hao-cal__nav', root)[n < 0 ? 0 : 1]; if (btn) btn.focus(); }
    }
    function moveFocus(days) {
      focusDate = new Date(focusDate.getFullYear(), focusDate.getMonth(), focusDate.getDate() + days, 12);
      view = new Date(focusDate.getFullYear(), focusDate.getMonth(), 1, 12);
      render('day');
    }
    function select(d) {
      selected = d; focusDate = new Date(d.getTime());
      view = new Date(d.getFullYear(), d.getMonth(), 1, 12);
      root.setAttribute('data-value', iso(d));
      render('day');
      emit(root, 'hao-change', { value: iso(d), date: d, lunar: lunar(d) });
    }
    root.addEventListener('click', function (e) {
      var b = e.target.closest('.hao-cal__day');
      if (b) select(parseDate(b.getAttribute('data-date')));
    });
    root.addEventListener('keydown', function (e) {
      var b = e.target.closest('.hao-cal__day');
      if (!b) return;
      var map = { ArrowLeft: -1, ArrowRight: 1, ArrowUp: -7, ArrowDown: 7 };
      if (map[e.key]) { e.preventDefault(); focusDate = parseDate(b.getAttribute('data-date')); moveFocus(map[e.key]); }
      else if (e.key === 'Home') { e.preventDefault(); focusDate = parseDate(b.getAttribute('data-date')); moveFocus(-((focusDate.getDay() + 6) % 7)); }
      else if (e.key === 'End') { e.preventDefault(); focusDate = parseDate(b.getAttribute('data-date')); moveFocus(6 - ((focusDate.getDay() + 6) % 7)); }
      else if (e.key === 'PageUp') { e.preventDefault(); focusDate = parseDate(b.getAttribute('data-date')); shift(-1); }
      else if (e.key === 'PageDown') { e.preventDefault(); focusDate = parseDate(b.getAttribute('data-date')); shift(1); }
    });
    render();
    root.haoCalendar = { get value() { return selected ? iso(selected) : null; }, select: select, shift: shift, render: render };
    return root.haoCalendar;
  }
  G.calendar = { create: calendarCreate, terms: null, source: null, lunar: lunar };

  /* ---------- 盖印 ---------- */
  G.stamp = function (root) {
    $$('.hao-seal--stamp', root).forEach(function (s) { replay(s, 'hao-seal--stamp'); });
    $$('.hao-stamp__text', root).forEach(function (s) { replay(s, 'hao-stamp__text'); });
  };

  /* ---------- 事件：全部委托在 document 上 ---------- */
  doc.addEventListener('click', function (e) {
    var t = e.target;
    if (!(t instanceof Element)) return;
    var opener = t.closest('[data-hao-open]');
    if (opener) { e.preventDefault(); modalOpen(doc.getElementById(opener.getAttribute('data-hao-open')), opener); return; }
    var closer = t.closest('[data-hao-close]');
    if (closer) { modalClose(closer.closest('.hao-scrim')); return; }
    if (t.classList.contains('hao-scrim') && modals.length && modals[modals.length - 1].scrim === t && !t.querySelector('[role="alertdialog"]')) { modalClose(t); return; }

    var mt = t.closest('[data-hao-menu]');
    if (mt) { e.preventDefault(); var menu = doc.getElementById(mt.getAttribute('data-hao-menu')); if (menuNow && menuNow.menu === menu) menuClose(); else if (menu) menuOpen(menu, mt); return; }
    if (menuNow) { if (t.closest('[role="menuitem"]') && menuNow.menu.contains(t)) { emit(t.closest('[role="menuitem"]'), 'hao-select'); menuClose(); } else if (!menuNow.menu.contains(t)) menuClose(false); }

    var tab = t.closest('[role="tab"]');
    if (tab && tab.closest('.hao-tabs')) { tabSelect(tab, false); return; }

    var tg = t.closest('[data-hao-toggle]');
    if (tg) {
      var on = tg.getAttribute('aria-pressed') !== 'true';
      var group = tg.closest('[data-hao-chips="single"]');
      if (group) { if (!on) return; $$('[data-hao-toggle]', group).forEach(function (c) { c.setAttribute('aria-pressed', 'false'); }); }
      tg.setAttribute('aria-pressed', on ? 'true' : 'false');
      var lab = tg.getAttribute(on ? 'data-label-on' : 'data-label-off');
      if (lab) tg.setAttribute('aria-label', lab);
      if (on && tg.classList.contains('hao-lamp')) replay(tg, 'hao-lamp--lit');
      emit(tg, 'hao-change', { pressed: on });
      return;
    }

    var sb = t.closest('.hao-stepper button');
    if (sb) { if (held) { held = false; return; } var st = sb.closest('.hao-stepper'); stepperStep(st, $$('button', st).indexOf(sb) === 0 ? -1 : 1); return; }

    var rb = t.closest('.hao-rate [role="radio"]');
    if (rb) { rateSet(rb.closest('.hao-rate'), rb, false); return; }

    var lo = t.closest('.hao-list[role="listbox"] [role="option"]');
    if (lo) { if (lo.getAttribute('aria-selected') !== 'true') listSelect(lo.closest('[role="listbox"]'), lo, false); return; }

    var tb = t.closest('[data-hao-toast]');
    if (tb) { var l = tb.closest('[lang]'); G.toast(tb.getAttribute('data-hao-toast'), { action: tb.getAttribute('data-hao-toast-action'), ok: tb.hasAttribute('data-hao-toast-ok'), lang: l && l.getAttribute('lang') }); return; }

    var sp = t.closest('[data-hao-stamp]');
    if (sp) { G.stamp(doc.getElementById(sp.getAttribute('data-hao-stamp'))); return; }

    var ub = t.closest('.hao-upload button');
    if (ub) { var fi = ub.closest('.hao-upload').querySelector('input[type="file"]'); if (fi) fi.click(); }
  });

  doc.addEventListener('keydown', function (e) {
    var t = e.target;
    if (e.key === 'Escape') {
      if (tipNow) { tipHide(); return; }
      if (menuNow) { e.preventDefault(); menuClose(); return; }
      if (modals.length) { e.preventDefault(); modalClose(); return; }
    }
    if (e.key === 'Tab' && modals.length) {
      var f = focusables(modals[modals.length - 1].panel);
      if (!f.length) { e.preventDefault(); return; }
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && (doc.activeElement === first || !modals[modals.length - 1].panel.contains(doc.activeElement))) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && doc.activeElement === last) { e.preventDefault(); first.focus(); }
    }
    if (!(t instanceof Element)) return;
    if (menuNow && menuNow.menu.contains(t)) {
      var items = menuItems(menuNow.menu), i = items.indexOf(doc.activeElement);
      if (e.key === 'ArrowDown') { e.preventDefault(); items[(i + 1) % items.length].focus(); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); items[(i - 1 + items.length) % items.length].focus(); }
      else if (e.key === 'Home') { e.preventDefault(); items[0].focus(); }
      else if (e.key === 'End') { e.preventDefault(); items[items.length - 1].focus(); }
      else if (e.key === 'Tab') { menuClose(false); }
      return;
    }
    var mt = t.closest('[data-hao-menu]');
    if (mt && (e.key === 'ArrowDown' || e.key === 'ArrowUp')) { e.preventDefault(); var menu = doc.getElementById(mt.getAttribute('data-hao-menu')); if (menu) { menuOpen(menu, mt); if (e.key === 'ArrowUp') { var its = menuItems(menu); its[its.length - 1].focus(); } } return; }
    var tab = t.closest('.hao-tabs [role="tab"]');
    if (tab) {
      var tabs = $$('[role="tab"]', tab.closest('[role="tablist"]')), n = tabs.indexOf(tab);
      if (e.key === 'ArrowRight') { e.preventDefault(); tabSelect(tabs[(n + 1) % tabs.length], true); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); tabSelect(tabs[(n - 1 + tabs.length) % tabs.length], true); }
      else if (e.key === 'Home') { e.preventDefault(); tabSelect(tabs[0], true); }
      else if (e.key === 'End') { e.preventDefault(); tabSelect(tabs[tabs.length - 1], true); }
      return;
    }
    var lo = t.closest('.hao-list[role="listbox"] [role="option"]');
    if (lo) {
      /* 方向键只移动焦点，回车或空格才选中：这类选项多半一选就生效，不让它跟着焦点走。 */
      var los = listOptions(lo.closest('[role="listbox"]')), ln = los.indexOf(lo), lt = null;
      if (e.key === 'ArrowDown') lt = los[Math.min(los.length - 1, ln + 1)];
      else if (e.key === 'ArrowUp') lt = los[Math.max(0, ln - 1)];
      else if (e.key === 'Home') lt = los[0];
      else if (e.key === 'End') lt = los[los.length - 1];
      if (lt) { e.preventDefault(); los.forEach(function (o) { o.tabIndex = o === lt ? 0 : -1; }); lt.focus(); }
      return;
    }
    var rb = t.closest('.hao-rate [role="radio"]');
    if (rb) {
      var rg = rb.closest('.hao-rate'), rs = $$('[role="radio"]', rg), k = rs.indexOf(rb);
      if (e.key === 'ArrowRight' || e.key === 'ArrowUp') { e.preventDefault(); rateSet(rg, rs[Math.min(rs.length - 1, k + 1)], true); }
      else if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') { e.preventDefault(); rateSet(rg, rs[Math.max(0, k - 1)], true); }
    }
  });

  doc.addEventListener('pointerdown', function (e) {
    var sb = e.target instanceof Element && e.target.closest('.hao-stepper button');
    if (!sb) return;
    var st = sb.closest('.hao-stepper'), dir = $$('button', st).indexOf(sb) === 0 ? -1 : 1;
    holdStop(); held = false;
    holdTimer = setTimeout(function () { held = true; holdRepeat = setInterval(function () { if (!stepperStep(st, dir)) holdStop(); }, 90); }, 450);
  });
  ['pointerup', 'pointercancel', 'pointerleave', 'blur'].forEach(function (n) { doc.addEventListener(n, holdStop, true); });

  doc.addEventListener('input', function (e) {
    var t = e.target;
    if (!(t instanceof Element)) return;
    if (t.classList.contains('hao-slider')) sliderSync(t);
    if (t.classList.contains('hao-field__input')) countSync(t);
  });
  doc.addEventListener('change', function (e) {
    var t = e.target;
    if (!(t instanceof Element) || t.type !== 'checkbox') return;
    if (t.hasAttribute('data-hao-checkall')) {
      $$('input[type="checkbox"][name="' + t.getAttribute('data-hao-checkall') + '"]:not([disabled])').forEach(function (b) { b.checked = t.checked; });
      t.indeterminate = false;
    } else if (t.name) {
      $$('[data-hao-checkall="' + t.name + '"]').forEach(checkallSync);
    }
  });
  function sliderSync(s) {
    var min = parseFloat(s.min) || 0, max = s.max === '' ? 100 : parseFloat(s.max);
    s.style.setProperty('--v', (max > min ? (parseFloat(s.value) - min) / (max - min) * 100 : 0) + '%');
  }

  doc.addEventListener('mouseover', function (e) {
    if (tipNow && e.target instanceof Node && (tipNow.tip.contains(e.target) || tipNow.target.contains(e.target))) { clearTimeout(tipLeave); return; }
    var t = e.target instanceof Element && e.target.closest('[data-hao-tip]');
    if (!t || (tipNow && tipNow.target === t)) return;
    clearTimeout(tipTimer);
    tipTimer = setTimeout(function () { tipShow(t); }, 500);
  });
  doc.addEventListener('mouseout', function (e) {
    var t = e.target instanceof Element && e.target.closest('[data-hao-tip]');
    if (t && !(e.relatedTarget instanceof Element && t.contains(e.relatedTarget))) { if (tipNow && tipNow.target === t) tipHideSoon(); else tipHide(); return; }
    if (tipNow && e.target instanceof Node && tipNow.tip.contains(e.target) && !(e.relatedTarget instanceof Node && tipNow.tip.contains(e.relatedTarget))) tipHideSoon();
  });
  doc.addEventListener('focusin', function (e) {
    var t = e.target instanceof Element && e.target.closest('[data-hao-tip]');
    if (t && t.matches(':focus-visible')) tipShow(t);
  });
  doc.addEventListener('focusout', function (e) { if (e.target instanceof Element && e.target.closest('[data-hao-tip]')) tipHide(); });
  window.addEventListener('scroll', tipHide, true);

  ['dragenter', 'dragover'].forEach(function (n) {
    doc.addEventListener(n, function (e) { var u = e.target instanceof Element && e.target.closest('.hao-upload'); if (u) { e.preventDefault(); u.classList.add('hao-upload--over'); } });
  });
  doc.addEventListener('dragleave', function (e) { var u = e.target instanceof Element && e.target.closest('.hao-upload'); if (u && !(e.relatedTarget instanceof Node && u.contains(e.relatedTarget))) u.classList.remove('hao-upload--over'); });
  doc.addEventListener('drop', function (e) {
    var u = e.target instanceof Element && e.target.closest('.hao-upload');
    if (!u) return;
    e.preventDefault();
    u.classList.remove('hao-upload--over');
    emit(u, 'hao-files', { files: e.dataTransfer ? e.dataTransfer.files : [] });
  });

  /* ---------- 初始化 ---------- */
  G.init = function (root) {
    root = root || doc;
    $$('[data-hao-calendar]', root).forEach(calendarCreate);
    $$('.hao-slider', root).forEach(sliderSync);
    $$('.hao-field__input', root).forEach(countSync);
    $$('[data-hao-checkall]', root).forEach(checkallSync);
    $$('.hao-stepper', root).forEach(function (st) { var o = st.querySelector('output'); if (o) stepperApply(st, parseFloat(o.textContent) || 0); });
    $$('.hao-tabs[role="tablist"]', root).forEach(function (list) {
      var tabs = $$('[role="tab"]', list), cur = tabs.filter(function (t) { return t.getAttribute('aria-selected') === 'true'; })[0] || tabs[0];
      tabs.forEach(function (t) { t.tabIndex = t === cur ? 0 : -1; var p = t.getAttribute('aria-controls') && doc.getElementById(t.getAttribute('aria-controls')); if (p) p.hidden = t !== cur; });
    });
    $$('.hao-rate', root).forEach(function (g) {
      var rs = $$('[role="radio"]', g), cur = rs.filter(function (b) { return b.getAttribute('aria-checked') === 'true'; })[0];
      rs.forEach(function (b) { b.tabIndex = b === (cur || rs[0]) ? 0 : -1; });
    });
    $$('.hao-list[role="listbox"]', root).forEach(function (list) {
      var opts = $$('[role="option"]', list), cur = opts.filter(function (o) { return o.getAttribute('aria-selected') === 'true'; })[0] || opts[0];
      opts.forEach(function (o) { o.tabIndex = o === cur ? 0 : -1; if (o.parentNode.tagName === 'LI') o.parentNode.setAttribute('role', 'none'); });
    });
    $$('[data-hao-menu]', root).forEach(function (t) { t.setAttribute('aria-haspopup', 'menu'); if (!t.hasAttribute('aria-expanded')) t.setAttribute('aria-expanded', 'false'); });
  };
  window.Hairline = G;
  if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', function () { G.init(); }); else G.init();
}());
