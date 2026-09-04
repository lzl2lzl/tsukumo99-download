---
name: 月云了桌宠网站
description: 深紫夜色里的角色化下载页与动作反应手册
colors:
  paper: "#fffaf0"
  body-muted: "#cbbfd7"
  label-quiet: "#9585a4"
  primary: "#8052ae"
  primary-bright: "#c49be8"
  night: "#17111f"
  night-deep: "#0e0b13"
  panel: "#24182f"
  panel-high: "#31203f"
  line: "rgba(225, 207, 240, 0.16)"
typography:
  display:
    fontFamily: '"PingFang SC", "Microsoft YaHei UI", "Noto Sans SC", system-ui, sans-serif'
    fontSize: "clamp(48px, 7vw, 86px)"
    fontWeight: 850
    lineHeight: 1.04
    letterSpacing: "-0.035em"
  headline:
    fontFamily: '"PingFang SC", "Microsoft YaHei UI", "Noto Sans SC", system-ui, sans-serif'
    fontSize: "clamp(28px, 4vw, 44px)"
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: "-0.025em"
  body:
    fontFamily: '"PingFang SC", "Microsoft YaHei UI", "Noto Sans SC", system-ui, sans-serif'
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.75
  label:
    fontFamily: '"PingFang SC", "Microsoft YaHei UI", "Noto Sans SC", system-ui, sans-serif'
    fontSize: "12px"
    fontWeight: 760
    lineHeight: 1.5
rounded:
  compact: "10px"
  action: "12px"
  container: "16px"
  hero: "28px"
  pill: "999px"
spacing:
  micro: "8px"
  compact: "14px"
  standard: "22px"
  section: "40px"
  major: "80px"
components:
  button-primary:
    backgroundColor: "#7950a1"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    rounded: "{rounded.action}"
    padding: "13px 18px"
    height: "50px"
  button-secondary:
    backgroundColor: "rgba(255, 255, 255, 0.035)"
    textColor: "{colors.body-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.action}"
    padding: "13px 18px"
    height: "50px"
  search-field:
    backgroundColor: "rgba(255, 255, 255, 0.035)"
    textColor: "{colors.paper}"
    typography: "{typography.body}"
    rounded: "{rounded.action}"
    padding: "0 14px"
    height: "48px"
  content-panel:
    backgroundColor: "{colors.panel}"
    textColor: "{colors.paper}"
    rounded: "{rounded.container}"
    padding: "25px"
---

# Design System: 月云了桌宠网站

## Overview

**Creative North Star: “深紫夜间使用手册”**

这是一个像角色在夜色桌面里递来说明书的视觉系统：安静、克制，有一点嘴硬，但所有操作都必须一眼看懂。深色背景承载大尺度奶白标题，紫色只用来标出行动、状态和可点击入口；真实的月云了立绘与 99 图标负责让页面仍然属于这个角色，而不是普通软件文档。

信息密度允许偏高，但必须靠清晰的网格、短句、细分隔线和稳定的上下节奏保持轻松。电脑端以不对称双栏和固定目录制造方向感，手机端重排为单栏并把目录变成可横滑的动作标签。

**Key Characteristics:**

- 深紫渐层背景、奶白高对比标题与低饱和正文。
- 超大、紧凑的中文标题配合细线账本式信息结构。
- 真实人物与 99 图标是主要识别资产，装饰保持节制。
- 行动入口醒目，说明区域平静，所有主要点击目标至少 44px 高。

## Colors

色彩像深夜桌面：背景从黑紫逐级抬高，奶白承载重点，葡萄紫只在行动和当前状态出现。

### Primary

- **葡萄行动紫**：用于主要按钮、选中标签和短距离进度标记。
- **月光亮紫**：用于当前项、细小序号、焦点和需要扫读的提示。

### Neutral

- **奶白纸面**：标题、关键结论和主要按钮文字。
- **雾紫正文**：说明文字和长段落，降低整页眩光。
- **暮紫标签**：辅助导航、注释和次要信息。
- **深夜背景**：页面主背景与最深底色。
- **墨紫面板**：卡片、提醒类型和操作示意区域的层级面。
- **月雾分隔线**：只承担结构，不承担装饰。

**The Rare Purple Rule.** 高亮紫只标记行动、选中和方向；不能把整段正文或大面积背景都染成亮紫。

**The Cream First Rule.** 最高层级信息始终先用奶白建立对比，不能用纯白与高饱和彩色争夺角色资产。

## Typography

**Display Font:** 系统中文无衬线栈，以苹方、微软雅黑 UI 和思源黑体为优先。

**Body Font:** 与展示字体同栈，通过字号、粗细和颜色形成层级。

**Character:** 标题宽厚、压缩、断行果断；正文克制、留足行距。字体不追求可爱装饰，角色感由文案、立绘与强烈的标题节奏共同完成。

### Hierarchy

- **Display**：只用于首屏主张，最多约 10 个中文字宽，并保持紧行距。
- **Headline**：章节标题，常与一段简短解释组成双栏标题带。
- **Title**：按钮、功能名和列表结论，粗度明显高于说明文字。
- **Body**：说明、触发结果和帮助文字，单段保持短小，长行不超过约 46rem。
- **Label**：平台、目录、序号和辅助状态，可使用少量字距，但不使用全大写英文替代中文。

**The One Glance Rule.** 每个内容块先出现一句粗体结论，再出现解释；禁止让用户先读完整段落才知道这块讲什么。

## Layout

全站内容宽度以 1120px 为上限，常规两侧至少保留 20px，手机端至少保留 14px。首屏使用不对称双栏，把主张与角色演示并置；长文使用 210px 目录加弹性正文栏，正文内部继续用“动作／结果”网格。

主要章节之间保留约 80–96px 的纵向距离；组件内部以 8、14、22 和 40px 形成从紧到松的节奏。900px 以下把主要双栏重排为单栏，660px 以下缩小页边距、标题和角色舞台，并把固定目录变成横向滚动标签。响应式只改变位置，不删除内容或功能。

## Elevation & Depth

系统以色阶和半透明描边为主、柔和阴影为辅。大舞台使用深色环境阴影把人物从页面中托起；主要按钮只带短而扩散的阴影；阅读列表通常保持平面，用细线和色面分层。

### Shadow Vocabulary

- **舞台环境影**：`0 34px 78px rgba(5, 2, 8, 0.4)`，只用于人物舞台等最大容器。
- **行动浮起影**：`0 14px 30px rgba(10, 5, 15, 0.32)`，用于主要行动按钮。
- **信息托底影**：`0 15px 34px rgba(6, 3, 9, 0.24)`，用于需从长文中被看见的说明条。

**The Flat Reading Rule.** 连续阅读内容默认平面化；阴影只给角色舞台、行动和少量关键说明，不能让每一块文字都变成悬浮卡片。

## Shapes

形状以 10–16px 的轻柔圆角为主，大型角色舞台使用 20–30px 圆角，平台与状态标签使用胶囊形。气泡保留一个更尖的小角作为角色语言的签名。分隔线保持细、低对比，不用厚边框模拟浮雕。

## Components

### Buttons

- **Shape:** 轻柔动作圆角，主要按钮通常为 12px，下载按钮可到 14px。
- **Primary:** 葡萄紫实底、奶白粗体、至少 44px 高；首页行动按钮为 50px 高。
- **Hover / Focus:** 可在精确指针设备上向上移动 2px；键盘焦点使用清楚的亮紫外圈；减少动画偏好下取消位移。
- **Secondary:** 透明夜色底、低对比描边和雾紫文字，不与主要行动争夺层级。

### Chips

- **Style:** 胶囊或紧凑圆角，未选中时安静透明，选中时使用墨紫或行动紫色面。
- **State:** 平台切换同时显示系统名称与最低版本；手机目录标签至少 44px 高并可横向滚动。

### Cards / Containers

- **Corner Style:** 常规内容面板使用 16px，大型人物舞台使用 28px。
- **Background:** 墨紫色阶或轻微透明白叠在深夜背景上。
- **Shadow Strategy:** 阅读卡片保持平面，大型舞台与关键说明使用对应阴影词汇。
- **Border:** 使用月雾分隔线保持边界可见。
- **Internal Padding:** 紧凑说明约 20–25px；大型舞台按构图留白。

### Inputs / Fields

- **Style:** 48px 高、12px 圆角、透明夜色底和细描边。
- **Focus:** 边框转为亮紫，并出现低透明的三像素焦点晕圈。

### Navigation

桌面导航是低调文字链接，当前页用奶白文字和一条亮紫细线标记；手机端仍保留主要入口，所有链接至少 44px 高。长文目录在桌面保持固定，在窄屏转换为横向滚动标签。

### 动作反应清单

每一行先写用户动作，再写角色结果，必要时补一条解释。紫色短线只标出行为升级的方向，不能变成装饰性的全宽渐变。

## Do's and Don'ts

### Do:

- **Do** 先用一句用户动作或结论命名内容块，再补充结果和解释。
- **Do** 在 Windows 与 macOS 入口不同时同时说明两个位置。
- **Do** 使用真实月云了立绘与 99 图标建立角色归属。
- **Do** 让桌面和手机拥有相同内容、可操作入口与安全说明。

### Don't:

- **Don't** 用伪造的系统截图或与真实产品不一致的界面演示。
- **Don't** 把每个段落都包成有阴影的卡片，或用渐变代替真实人物素材。
- **Don't** 用软件内部模块名组织面向用户的说明。
- **Don't** 为了视觉完整而隐藏当前安装包的版本、签名状态或系统要求。
