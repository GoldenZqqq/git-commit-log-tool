<div align="center">

# 🚀 Git Commit Log Extractor

*The Ultimate Developer's Daily Report Generator*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/yourusername/git-commit-log-tool)
[![GUI](https://img.shields.io/badge/GUI-tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/yourusername/git-commit-log-tool)

**Language / 语言**: [🇺🇸 English](#english) | [🇨🇳 中文](#中文)

---

</div>

## 🇺🇸 English

### 📖 Overview

**Git Commit Log Extractor** is a powerful, user-friendly tool designed to automatically extract and generate daily work reports from multiple Git repositories. Perfect for developers who need to quickly summarize their daily coding activities for standups, reports, or personal tracking.

### ✨ Key Features

- 🔍 **Smart Repository Discovery** - Automatically scans and finds all Git repositories in specified directories
- 👤 **Author-Based Filtering** - Extract commits only from specific authors
- 📅 **Flexible Date Range** - Support for single day or custom date range extraction
- 🎯 **Detailed & Summary Views** - Choose between detailed logs or concise summaries
- 🏷️ **Project Name Mapping** - Customize project names for better readability
- 🔄 **Auto-Pull Support** - Optionally pull latest changes before extraction
- 🌿 **Branch Control** - Extract from current branch or all branches
- 🖥️ **Beautiful GUI** - Intuitive graphical interface for easy configuration
- 📦 **Portable Executable** - Standalone `.exe` file for Windows users
- ⚙️ **Configuration Management** - Save and load settings automatically

### 🎯 Perfect For

- 📊 **Daily Standups** - Quick summary of yesterday's work
- 📝 **Weekly Reports** - Comprehensive overview of accomplishments
- 🔍 **Code Review Prep** - Track what's been changed and where
- 📈 **Project Management** - Monitor development progress across multiple projects
- 🎭 **The Art of Looking Busy** - Generate impressive-looking work logs! 😉

### 🚀 Quick Start

#### Method 1: GUI Application (Recommended)

1. **Download & Run**
   ```bash
   git clone https://github.com/yourusername/git-commit-log-tool.git
   cd git-commit-log-tool
   python gui.py
   ```

2. **Configure Settings**
   - Set your repository root directory
   - Enter your Git author name
   - Choose output directory
   - Adjust advanced options as needed

3. **Extract Logs**
   - Click "🚀 Start Extraction" and watch the magic happen!

#### Method 2: Command Line

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure**
   ```bash
   # Edit config.yaml with your settings
   nano config.yaml
   ```

3. **Run**
   ```bash
   python main.py
   ```

### 📦 Building Executable

Want to create a standalone executable? We've got you covered!

```bash
python build.py
```

This will create:
- `dist/GitCommitTool.exe` - Standalone executable
- `GitCommitTool_Portable/` - Portable package with all files

### 🛠️ Configuration

The tool uses a flexible YAML configuration file:

```yaml
# Repository settings
root_directory: "C:\\workspace"          # Root directory to scan
author: "YourGitUsername"                # Git author name
output_directory: "~/Desktop"            # Output location

# Date range (optional)
start_date: "2024-01-01"                # Start date (YYYY-MM-DD)
end_date: "2024-01-31"                  # End date (YYYY-MM-DD)

# Output options
detailed_output: true                    # Include detailed logs
show_project_and_branch: true          # Show project/branch names

# Advanced options
pull_latest_code: false                 # Pull before extraction
extract_all_branches: false            # Extract from all branches

# Project name mapping
project_names:
  "my-project(master)": "My Awesome Project - "
  "api-service(develop)": "Backend API - "
```

### 📋 Sample Output

```
🎯 Summary of Commits (2024-01-15):

My Awesome Project - Added user authentication system
My Awesome Project - Fixed login validation bug
Backend API - Implemented new REST endpoints
Backend API - Updated database schema
Mobile App - Enhanced UI responsiveness

📊 Total: 5 commits across 3 projects
⏱️ Generated on: 2024-01-15 18:30:22
```

### 🎨 Screenshots

<div align="center">

![GUI Main Interface](docs/screenshots/gui-main.png)
*Modern and intuitive GUI interface*

![Configuration Panel](docs/screenshots/gui-config.png)
*Easy-to-use configuration panel*

</div>

### 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 🙏 Acknowledgments

- Thanks to all contributors who have helped improve this tool
- Inspired by the daily struggles of developers everywhere
- Built with ❤️ and lots of ☕

---

## 🇨🇳 中文

### 📖 项目简介

**Git 提交日志提取工具**是一款功能强大、使用便捷的开发者工具，专为自动化提取多个 Git 仓库的提交记录并生成工作日报而设计。无论是日常站会、工作汇报还是个人记录，这款工具都能让你轻松搞定！

### ✨ 核心特性

- 🔍 **智能仓库发现** - 自动扫描并找到指定目录下的所有 Git 仓库
- 👤 **作者筛选** - 按指定作者提取提交记录
- 📅 **灵活日期范围** - 支持单日或自定义日期范围提取
- 🎯 **详细&摘要视图** - 可选择详细日志或简洁摘要
- 🏷️ **项目名称映射** - 自定义项目名称，提高可读性
- 🔄 **自动拉取支持** - 可选择在提取前拉取最新代码
- 🌿 **分支控制** - 从当前分支或所有分支提取
- 🖥️ **精美GUI界面** - 直观的图形界面，配置简单
- 📦 **便携执行文件** - Windows 用户可使用独立的 `.exe` 文件
- ⚙️ **配置管理** - 自动保存和加载设置

### 🎯 适用场景

- 📊 **每日站会** - 快速总结昨天的工作内容
- 📝 **周报月报** - 全面展示工作成果
- 🔍 **代码审查准备** - 追踪代码变更
- 📈 **项目管理** - 监控多项目开发进度
- 🎭 **摸鱼神器** - 生成看起来很厉害的工作日志！😉

### 🚀 快速开始

#### 方式一：GUI应用程序（推荐）

1. **下载并运行**
   ```bash
   git clone https://github.com/yourusername/git-commit-log-tool.git
   cd git-commit-log-tool
   python gui.py
   ```

2. **配置设置**
   - 设置仓库根目录
   - 输入 Git 作者名
   - 选择输出目录
   - 根据需要调整高级选项

3. **提取日志**
   - 点击 "🚀 开始提取日志" 按钮，见证奇迹发生！

#### 方式二：命令行

1. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

2. **配置设置**
   ```bash
   # 编辑 config.yaml 文件
   nano config.yaml
   ```

3. **运行程序**
   ```bash
   python main.py
   ```

### 📦 构建可执行文件

想要创建独立的可执行文件？我们为你准备了自动化脚本！

```bash
python build.py
```

这将创建：
- `dist/GitCommitTool.exe` - 独立可执行文件
- `GitCommitTool_Portable/` - 包含所有文件的便携版

### 🛠️ 配置说明

工具使用灵活的 YAML 配置文件：

```yaml
# 仓库设置
root_directory: "C:\\workspace"          # 扫描的根目录
author: "你的Git用户名"                   # Git 作者名
output_directory: "~/Desktop"            # 输出位置

# 日期范围（可选）
start_date: "2024-01-01"                # 开始日期 (YYYY-MM-DD)
end_date: "2024-01-31"                  # 结束日期 (YYYY-MM-DD)

# 输出选项
detailed_output: true                    # 包含详细日志
show_project_and_branch: true          # 显示项目/分支名

# 高级选项
pull_latest_code: false                 # 提取前拉取最新代码
extract_all_branches: false            # 从所有分支提取

# 项目名称映射
project_names:
  "my-project(master)": "我的项目 - "
  "api-service(develop)": "后端API - "
```

### 📋 输出示例

```
🎯 提交记录摘要 (2024-01-15):

我的项目 - 添加用户认证系统
我的项目 - 修复登录验证bug
后端API - 实现新的REST接口
后端API - 更新数据库架构
移动应用 - 增强UI响应性

📊 总计：3个项目共5次提交
⏱️ 生成时间：2024-01-15 18:30:22
```

### 🎨 界面截图

<div align="center">

![GUI主界面](docs/screenshots/gui-main.png)
*现代化直观的GUI界面*

![配置面板](docs/screenshots/gui-config.png)
*易于使用的配置面板*

</div>

### 🤝 贡献指南

我们欢迎任何形式的贡献！请查看我们的[贡献指南](CONTRIBUTING.md)了解详情。

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

### 🙏 致谢

- 感谢所有为改进此工具做出贡献的开发者
- 灵感来源于全世界开发者的日常需求
- 用 ❤️ 和大量的 ☕ 精心打造

---

<div align="center">

### 🌟 如果这个项目对你有帮助，请给个星标！ 

**Made with ❤️ by developers, for developers**

</div>