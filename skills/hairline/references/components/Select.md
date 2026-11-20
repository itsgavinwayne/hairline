# Select · 下拉选择

从六项以上的列表里选一项。样子照 iOS 的弹出按钮：淡染的底，石青的字，右边一对上下箭头。

`<span class="hao-select">` 包住原生的 `<select>`。选项由你提供。

- 用原生 `<select>`：在手机上它会唤起系统自己的选择器，这正是 iOS 用户习惯的。不要自己画下拉面板。
- 按钮的宽度跟着当前选项走，不撑满一行。要撑满时加 `hao-select--block`。
- 单独使用时，外面照 `TextField` 的结构放标签和说明，标签在上方。
- 放进 `ListGroup` 的行里时加 `hao-select--plain`：去掉底色，值靠右，颜色退成 `ink-secondary`，和 iOS 设置里的写法一样。行的标题用 `<label>`，接到 `<select>` 的 `id`。
- 上下一对箭头表示「点开是一列选项」；只朝下的箭头留给折叠面板。
- 五项以内用单选，全部摆出来比藏起来好。
- 选项按使用者能预期的顺序排（时间、字母、常用度），不要随意排。

**无障碍**

- 用原生 `<select>`，高 44px：Tab 走到，空格或方向键打开系统的选择器，都是浏览器自带；标签用 `for` 接到它的 `id`。
- 聚焦时描一圈 `focus` 色的边。
- 右侧的箭头是 `.hao-select::after` 画的，读屏读不到；读到的是 `<option>` 的文字。

## 标记

### 中文

```html
<div class="hao-field" style="width:340px">
  <label class="hao-field__label" for="s">存到</label>
  <span class="hao-select"><select id="s"><option>随笔</option><option>读书</option><option>工作</option><option>旅行</option></select></span>
  <span class="hao-field__hint">之后可以随时移动</span>
</div>
<div style="width:340px;margin-top:var(--hao-space-6)">
  <ul class="hao-list">
    <li><div class="hao-list__row"><label class="hao-list__title" for="s2">存到</label><span class="hao-select hao-select--plain"><select id="s2"><option>随笔</option><option>读书</option><option>工作</option><option>旅行</option></select></span></div></li>
    <li><div class="hao-list__row"><label class="hao-list__title" for="s3">排序</label><span class="hao-select hao-select--plain"><select id="s3"><option>最近编辑</option><option>创建时间</option><option>标题</option></select></span></div></li>
  </ul>
</div>
```

### English

```html
<div class="hao-field" style="width:340px">
  <label class="hao-field__label" for="s-en">Save to</label>
  <span class="hao-select"><select id="s-en"><option>Essays</option><option>Reading</option><option>Work</option><option>Travel</option></select></span>
  <span class="hao-field__hint">You can move it later</span>
</div>
<div style="width:340px;margin-top:var(--hao-space-6)">
  <ul class="hao-list">
    <li><div class="hao-list__row"><label class="hao-list__title" for="s2-en">Save to</label><span class="hao-select hao-select--plain"><select id="s2-en"><option>Essays</option><option>Reading</option><option>Work</option><option>Travel</option></select></span></div></li>
    <li><div class="hao-list__row"><label class="hao-list__title" for="s3-en">Sort by</label><span class="hao-select hao-select--plain"><select id="s3-en"><option>Last edited</option><option>Date created</option><option>Title</option></select></span></div></li>
  </ul>
</div>
```
