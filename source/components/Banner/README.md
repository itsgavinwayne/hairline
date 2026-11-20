页面内的一条提示，说明发生了什么、接下来怎么办。

`.hao-banner` 里放一个 20px 的图标和一段文字，标题用 `<strong>`。色调类：默认（信息）、`hao-banner--jade`（成功）、`hao-banner--amber`（提醒）、`hao-banner--seal`（出错）。你提供图标、标题和说明。

- 每种色调配固定的图标：`hao-icon--info`、`hao-icon--success`、`hao-icon--warning`、`hao-icon--error`。图标和标题一起表达状态，不只靠底色。
- 标题说结果（「已发布」），说明说影响或下一步。不道歉，不用感叹号。
- 出错用 `role="alert"`，其余用 `role="status"`。
- 一屏最多一条；多条消息排队出现。
