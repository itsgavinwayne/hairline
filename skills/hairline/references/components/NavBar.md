# NavBar · 导航栏

页面顶部的导航栏，告诉人现在在哪、怎么回去、这一页最主要的动作是什么。

`<header class="hao-nav">` 里放一个 `.hao-nav__bar`，三格：左边返回（`.hao-nav__action`，带左箭头和上一页的名字），中间 `.hao-nav__title`，右边一个动作。首页这类顶层页面用 `hao-nav--large`：栏下再放 `.hao-nav__large`，里面是宋体大标题，右侧可放一方小印。你提供标题、返回目标和动作。

- 标准栏用 `material` 毛玻璃，内容从下面滚过；大标题栏是透明的，直接坐在 `bg` 上。
- 右侧只放一个动作。确认类的动作（完成、保存）加 `hao-nav__action--strong`。更多动作收进底部弹层。
- 返回按钮写上一页的名字，不写「返回」。标题太长时省略号截断，不换行，不缩字号。
- 栏内标题用黑体 `headline`；宋体只出现在大标题里。
- 纹样和题签不进导航栏。大标题右侧的小印是这一屏唯一的朱砂。

**无障碍**

- 左右动作是真链接、真按钮，高 44px，Tab 走得到；聚焦时描 `focus` 色的边。
- 返回的箭头图标照预览写 `aria-hidden="true"`，按钮的名字就是旁边那几个字。
- 页面题目写成标题元素（预览里 `.hao-nav__title` 是 `<h1>`），读屏能按标题跳到这一页。
- 大标题栏的小印是装饰，照预览写 `aria-hidden="true"`。

## 标记

### 中文

```html
<div class="hao-stack" style="gap:var(--hao-space-6)">
  <header class="hao-nav" style="border-radius:var(--hao-radius-md)">
    <div class="hao-nav__bar">
      <a class="hao-nav__action" href="#"><i class="hao-icon hao-icon--chevron-left" aria-hidden="true"></i>札记</a>
      <h1 class="hao-nav__title">晨间札记</h1>
      <button class="hao-nav__action hao-nav__action--strong">完成</button>
    </div>
  </header>
  <header class="hao-nav hao-nav--large">
    <div class="hao-nav__bar">
      <span></span><span></span>
      <button class="hao-nav__action">编辑</button>
    </div>
    <div class="hao-nav__large"><h1>札记</h1><span class="hao-seal hao-seal--sm hao-seal--outline" aria-hidden="true">印</span></div>
  </header>
</div>
```

### English

```html
<div class="hao-stack" style="gap:var(--hao-space-6)">
  <header class="hao-nav" style="border-radius:var(--hao-radius-md)">
    <div class="hao-nav__bar">
      <a class="hao-nav__action" href="#"><i class="hao-icon hao-icon--chevron-left" aria-hidden="true"></i>Notes</a>
      <h1 class="hao-nav__title">Morning note</h1>
      <button class="hao-nav__action hao-nav__action--strong">Done</button>
    </div>
  </header>
  <header class="hao-nav hao-nav--large">
    <div class="hao-nav__bar">
      <span></span><span></span>
      <button class="hao-nav__action">Edit</button>
    </div>
    <div class="hao-nav__large"><h1>Notes</h1><span class="hao-seal hao-seal--sm hao-seal--outline" lang="zh" aria-hidden="true">印</span></div>
  </header>
</div>
```
