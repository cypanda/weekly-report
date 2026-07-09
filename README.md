# 🗓️ Weekly Report | Mac 私人时间管理小助手
[🇺🇸 English](./README-EN.md) | **🇨🇳 简体中文**

习惯用苹果日历记录日程，周末想复盘时却发现：**苹果原生不支持周统计，手动算账又太耗时间？**

Weekly Report 就是为你准备的极简小助手！只需在终端敲一行指令，它就能自动读取你的本地日历，秒速核算时间花费，并结合 AI 生成一份排版精美的 Markdown 时间周报。

---

## 一、✨ 核心亮点

* 📊 **全自动统计**：一键自动计算本周各分类任务投入时长。
* 🤖 **AI 深度复盘**：自动聚合琐碎事项，提炼本周核心投入事项。
* ⚖️ **直观环比对比**：图表化展示时间分配，并自动与上周数据进行对比。
* 🔒 **隐私绝对安全**：纯本地运行，API Key 与日历数据、周报本地化存储，绝不上传云端。

---

## 二、💻 极速安装
### 1、支持环境
- 目前仅支持macos的日历。

### 2、快速安装
无需克隆代码！只要你的 Mac 有终端和 Python 环境，直接复制这行命令并回车，即可一键下载并安装：

```bash
pip3 install git+https://github.com/你的用户名/你的项目名.git

```

### 3、 ⚠️ **Mac 用户的常见小插曲（必看！）**
> 如果安装进度条跑完后，你在终端输入 `weekly-report` 却提示 `command not found`，别慌！这是 Mac 系统的常见保护机制。
> 只需要复制并执行下面这两行代码，把安装路径告诉系统即可完美解决：
> 
> ```bash
> echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc
> source ~/.zshrc
> 
> ```
> 
> *(注：如果你的 Python 为其他版本，请将路径中的 3.9 替换为实际的版本号)*

---

## 三、🚀 快速上手

安装成功后，你在电脑的**任何位置**都可以随时唤醒小助手，生成周报！只需掌握两个简单指令：

### 1. ⚙️ 初始化配置（仅首次使用需配置）

```bash
weekly-report init

```

- *主要跟着终端提示，根据你实际的日历分类，配置你需要统计的日历、配置 AI 模型（兼容 DeepSeek/OpenAI/硅基流动等主流平台），并选择周报的保存位置。*

### 2. 🪄 召唤本周周报

每到周末，泡一杯咖啡，在终端敲下：

```bash
weekly-report run

```

*静静等待几秒钟，一份数据详实、排版精美的 Markdown 周报就会自动生成在你指定的文件夹里啦！*

---
### 3、快捷指令：搭配 Mac“快捷指令”实现一键生成

如果你觉得每次打开终端还是有点麻烦，我们可以利用 Mac 自带的「快捷指令 (Shortcuts)」App，把生成周报变成顶部菜单栏里的一个优雅按钮！

**配置步骤：**

1. 打开 Mac 系统自带的 **“快捷指令”** App。
    
2. 点击顶部菜单栏的 **“文件” -> “新建快捷指令”**。
    
3. 在右侧的搜索框里搜索 **“运行 Shell 脚本” (Run Shell Script)**，并双击把它添加到左侧的编辑区。
    
4. 将脚本编辑区的内容替换为以下代码：

Bash

```
export PATH="$HOME/Library/Python/3.9/bin:$PATH"

# 告诉程序，本次运行来自于快捷指令按钮
export WEEKLY_REPORT_SOURCE="快捷指令"

if weekly-report run > /tmp/weekly_report_log.txt 2>&1; then
    osascript -e 'display notification "✅ 本周周报已成功生成，快去文件夹看看吧！" with title "Weekly Report" subtitle "时间魔法生效 ✨"'
else
    osascript -e 'display notification "❌ 糟糕，生成失败了！请打开终端运行 weekly-report run 查看具体报错。" with title "Weekly Report"'
fi
```


**🎉 搞定！** 现在你的快捷指令就多了一个指令。每到周末，只需用鼠标轻轻一点，排版完美的 Markdown 周报就会像魔法一样默默生成在你的专属文件夹里啦！
## 四、🤝 参与贡献

这个小工具最初只是为了拯救被“手动周报”折磨的我。如果它也恰好帮到了你，欢迎给我点个 **Star ⭐️**！

遇到 Bug 或者有新点子？随时欢迎提交 Issue，我们一起让它变得更好用～
