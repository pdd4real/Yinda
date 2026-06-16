# 音达康护 AudioCare

> 基于音频感知的智慧居家养老系统

面向独居、高龄、慢病风险老人的居家养老系统。以声音事件检测补足视频监控盲区，以视频跌倒复核确认风险，通过 Web 总控平台和小程序派单形成完整闭环。

## 技术栈

- **声音事件检测 (SED)**: ATST-Frame 自监督音频帧级表示
- **音源增强**: TRUNet 降噪增强
- **视频复核**: YOLOv5 跌倒行为检测
- **前端**: 纯静态 HTML/CSS/JS，响应式设计

## 在线演示

访问 [GitHub Pages](https://your-username.github.io/your-repo/) 查看在线演示。

- 首页：系统介绍与背景
- 总控台：点击「登录演示」→ 账号 `admin` / 密码 `admin`

## 本地运行

直接用浏览器打开 `index.html`，或使用任意静态文件服务器：

```bash
# Python 3
python -m http.server 8080

# Node.js (npx)
npx serve .
```

## 项目结构

```
├── index.html      # 首页（系统介绍）
├── demo.html       # 社区总控演示
├── styles.css      # 全局样式
├── app.js          # 交互逻辑
└── assets/         # 图片资源
```
