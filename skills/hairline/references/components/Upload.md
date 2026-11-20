# Upload · 上传

选文件或把文件拖进来的区域。

`.hao-upload` 里放一句 `<strong>` 说明、一行限制、一个 `hao-btn--tinted` 按钮（真正的 `<input type="file">` 藏在按钮后面）。拖到上方时加 `hao-upload--over`。文字由你提供。

- 按钮是必须的：拖放只是鼠标用户的捷径，触屏和键盘都靠按钮。
- 把格式和大小限制事先写出来，不要等传错了才说。
- 传的过程用 `Progress` 的进度条，每个文件一行；传完用 `ListGroup` 列出文件名，可以删除。
- 传错了在那一行说明原因和怎么办（「超过 10 MB，压缩后再试」）。
- 边框是一圈针脚：一段一段的短线，圆头，和针脚纹样是同一种线。拖到上方时针脚变成 `tint`。

**行为**（加载了行为脚本时）

- 把文件拖到上方时自动切到「拖入」的样子，放下后发出 `hao-files` 事件，带上文件列表。
- 里面放一个隐藏的 `<input type="file">`，点按钮就会打开系统的选文件窗口。上传本身和进度需要自己接。

## 标记

### 中文

```html
<div class="hao-upload" style="max-width:420px">
  <strong>把图片拖到这里</strong>
  <span>支持 JPG、PNG，单张不超过 10 MB</span>
  <button class="hao-btn hao-btn--tinted">选择图片</button>
</div>
```

### English

```html
<div class="hao-upload" style="max-width:420px">
  <strong>Drag images here</strong>
  <span>JPG or PNG, up to 10 MB each</span>
  <button class="hao-btn hao-btn--tinted">Choose images</button>
</div>
```
