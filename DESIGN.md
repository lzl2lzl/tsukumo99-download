---
name: 月云了桌宠网站
description: 面向公众的简洁产品预览、下载与使用说明
colors:
  paper: "#f7f3f8"
  ink: "#271d2c"
  body-muted: "#685f6d"
  label-quiet: "#8a808f"
  primary: "#725095"
  primary-dark: "#5f407e"
  wash: "#ebe1ef"
  line: "#dcd2df"
typography:
  display:
    fontFamily: '"PingFang SC", "Microsoft YaHei UI", "Noto Sans SC", system-ui, sans-serif'
    fontSize: "clamp(48px, 7vw, 82px)"
    fontWeight: 820
    lineHeight: 1.04
    letterSpacing: "-0.03em"
  headline:
    fontFamily: '"PingFang SC", "Microsoft YaHei UI", "Noto Sans SC", system-ui, sans-serif'
    fontSize: "clamp(27px, 4vw, 38px)"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  body:
    fontFamily: '"PingFang SC", "Microsoft YaHei UI", "Noto Sans SC", system-ui, sans-serif'
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.75
  label:
    fontFamily: '"PingFang SC", "Microsoft YaHei UI", "Noto Sans SC", system-ui, sans-serif'
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1.5
rounded:
  compact: "10px"
  action: "12px"
  speech: "14px"
  pill: "999px"
spacing:
  micro: "8px"
  compact: "14px"
  standard: "22px"
  section: "40px"
  major: "80px"
---

# Design System: 月云了桌宠网站

## Direction

网站是公开、正式的产品预览与下载入口，不是营销落地页，也不是开发文档。页面只回答产品名称、系统版本、下载方式、基本玩法和常用入口。语言直接，不写品牌宣言，不把简单功能包装成卖点。

视觉采用浅灰紫纸面、深色正文和单一葡萄紫操作色。月云了立绘与 99 图标承担产品识别，其他装饰保持克制。人物可以说一句符合角色性格的话，说明文字本身保持准确、平静。

## Layout

内容宽度不超过 1040px。下载页首屏在桌面端使用文字与人物双栏，手机端自然改为单栏；说明页宽度不超过 900px，以连续文字和分隔线组织内容。主要段落之间使用明显留白，不使用同尺寸功能卡片、编号流程或侧边目录。

## Components

主要下载按钮使用紫色实底，备用下载与返回入口使用细边框。平台切换采用普通文字标签与下划线，不使用胶囊容器。玩法与帮助内容按“动作／结果”成对排列，依靠分隔线建立节奏。所有可点击目标至少 44px 高，并保留清晰的键盘焦点。

## Copy

产品名直接写“月云了桌宠”。首页首句只说明它在桌面上怎样互动，不使用“陪伴”“体验”“完整生态”等宣传词。必要的系统要求、未签名状态和提醒暂停限制必须保留，但每项只说一次。使用说明控制在一次短阅读内，详细内部规则不放在公开文档中。

## Responsive and Accessibility

桌面和手机提供相同下载与说明内容。页面不能横向滚动，正文对比度满足日常阅读，图片带有明确替代文字，标签页支持键盘左右键切换；减少动画偏好下取消人物入场动画。
