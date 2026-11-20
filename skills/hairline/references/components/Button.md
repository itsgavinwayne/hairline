# Button · 按钮

触发一个动作的按钮，一屏只放一个主按钮。

用 `<button class="hao-btn">`，文字由你提供，写清按下去会发生什么（「保存修改」，不写「确定」）。

| 类名 | 用在哪里 |
| --- | --- |
| `hao-btn` | 主按钮，`tint` 填充。一屏一个。 |
| `hao-btn--tinted` | 次级动作，`tint-wash` 底。 |
| `hao-btn--plain` | 取消、跳过这类退路，或主按钮旁边的第二个去处，只有文字。 |
| `hao-btn--seal` | 删除等不可撤销的动作。它算这一屏的朱砂，别再放印章。 |
| `hao-btn--sm` | 列表行内的小号胶囊，高 32px；外面要留够 44px 的触控区。 |
| `hao-btn--block` | 撑满容器宽度，用在表单底部。 |

- 不要把两个主按钮并排放。
- 按钮文字不换行，不超过六个字。
- 禁用时加 `disabled` 属性，并在旁边说明为什么不能点。禁用的按钮是灰底灰字，不是变淡的主按钮，免得和次级按钮混。
- 点了之后要等的，加 `aria-busy="true"`：按钮前面出现一个小圆环，文字改成进行时（「正在保存」），期间不能再点。完成后用轻提示说「已保存」。
- 按钮最小宽 88px（小号 64px），两个字的按钮也有足够的分量；纯文字按钮不设最小宽度。

## 标记

### 中文

```html
<div class="hao-stack" style="max-width:none">
  <div class="hao-row">
    <button class="hao-btn">保存修改</button>
    <button class="hao-btn hao-btn--tinted">存为草稿</button>
    <button class="hao-btn hao-btn--plain">取消</button>
    <button class="hao-btn hao-btn--seal">删除这条札记</button>
  </div>
  <div class="hao-row">
    <button class="hao-btn hao-btn--sm">关注</button>
    <button class="hao-btn hao-btn--sm hao-btn--tinted">已关注</button>
    <button class="hao-btn" disabled>保存修改</button>
    <button class="hao-btn" aria-busy="true">正在保存</button>
  </div>
</div>
```

### English

```html
<div class="hao-stack" style="max-width:none">
  <div class="hao-row">
    <button class="hao-btn">Save changes</button>
    <button class="hao-btn hao-btn--tinted">Save as draft</button>
    <button class="hao-btn hao-btn--plain">Cancel</button>
    <button class="hao-btn hao-btn--seal">Delete this note</button>
  </div>
  <div class="hao-row">
    <button class="hao-btn hao-btn--sm">Follow</button>
    <button class="hao-btn hao-btn--sm hao-btn--tinted">Following</button>
    <button class="hao-btn" disabled>Save changes</button>
    <button class="hao-btn" aria-busy="true">Saving</button>
  </div>
</div>
```
