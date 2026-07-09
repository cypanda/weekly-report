# 🗓️ Weekly Report | Your Mac Personal Time Management Assistant
**🇺🇸 English** | [🇨🇳 简体中文](./README.md)
Are you used to tracking your schedule with Apple Calendar, only to find out at the end of the week that Apple natively doesn't support weekly statistics, and calculating it manually takes forever?

Weekly Report is the minimalist assistant built exactly for this! With just one terminal command, it automatically reads your local calendar, instantly calculates your time spent, and teams up with AI to generate a beautifully formatted Markdown weekly report.

## 🌟 Core Highlights
- 📊 Fully Automated Stats: Calculate your weekly time investment across different categories with one click.

- 🤖 AI Deep Review: Automatically aggregates scattered tasks and extracts your core focus for the week.

- ⚖️ Intuitive Comparison: Visualizes your time allocation with charts and automatically compares it with last week's data.

- 🔒 Absolute Privacy: 100% local execution. Your API Keys, calendar data, and reports are stored locally. Zero cloud uploads.

## 💻 Quick Installation
### 1. Requirements
Currently, this tool exclusively supports the macOS native Calendar.

### 2. One-Click Install
No need to clone the repository! As long as your Mac has a terminal and a Python environment, just copy this command and hit Enter to install:

Bash
pip3 install git+https://github.com/YourUsername/YourProjectName.git
(Remember to replace the URL with your actual GitHub repo link)

### 3. ⚠️ Common Hiccup for Mac Users (Must Read!)
If the installation completes but your terminal says command not found: weekly-report, don't panic! This is a common macOS security mechanism.

Just copy and run these two lines to tell your system where the tool is installed:

Bash
echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
(Note: If you are using a different Python version, simply replace 3.9 with your actual version number)

## 🚀 Getting Started
Once installed, you can summon your assistant from anywhere on your Mac using just two simple commands:

### 1. ⚙️ Initialization (First-time setup only)
Bash
weekly-report init
Follow the gentle terminal prompts to map your actual calendar categories, configure your AI model (compatible with DeepSeek, OpenAI, SiliconFlow, etc.), and choose where to save your reports.

### 2. 🪄 Summon Your Weekly Report
Every weekend, grab a cup of coffee and type this in your terminal:

Bash
weekly-report run
Wait a few seconds, and a data-rich, beautifully formatted Markdown report will magically appear in your specified folder!

### 🎁 Bonus: One-Click Generation via Apple "Shortcuts"
If opening the terminal every time feels tedious, we can use the built-in Mac "Shortcuts" App to turn this into an elegant button in your top menu bar!

Setup Steps:

Open the native Shortcuts App on your Mac.

Click File -> New Shortcut in the top menu bar.

Search for "Run Shell Script" in the right sidebar and double-click to add it to the editor.

Replace the code in the script editor with the following:

Bash
```
export PATH="$HOME/Library/Python/3.9/bin:$PATH"

# Tell the program this run is triggered by Shortcuts
export WEEKLY_REPORT_SOURCE="Shortcuts"

if weekly-report run > /tmp/weekly_report_log.txt 2>&1; then
    osascript -e 'display notification "✅ This week'\''s report has been successfully generated!" with title "Weekly Report" subtitle "Time Magic Applied ✨"'
else
    osascript -e 'display notification "❌ Oops, generation failed! Run `weekly-report run` in terminal for details." with title "Weekly Report Error"'
fi
```

🎉 All set! Now you have a dedicated shortcut. Every weekend, just a gentle mouse click, and your perfect Markdown report will silently generate in your folder like magic!

## 🤝 Contributing
This little tool was originally built to save myself from the torture of "manual weekly reporting." If it happens to help you too, please consider giving it a Star ⭐️!

Found a bug or have a cool idea? Feel free to submit an Issue or PR. Let's make it better together!