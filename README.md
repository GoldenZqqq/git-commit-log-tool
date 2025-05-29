<div align="center">

# 🚀 Git Commit Log Extractor

*The Ultimate Developer's Daily Report Generator*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/yourusername/git-commit-log-tool)
[![GUI](https://img.shields.io/badge/GUI-Material_UI-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/yourusername/git-commit-log-tool)

**Language / 语言**: [🇺🇸 English](#english) | [🇨🇳 中文](#中文)

---

</div>

## English

### 📖 Overview

**Git Commit Log Extractor** is a powerful, user-friendly tool designed to automatically extract and generate daily work reports from multiple Git repositories. Perfect for developers who need to quickly summarize their daily coding activities for standups, reports, or personal tracking.

### ✨ Key Features

- 🔍 **Smart Repository Discovery** - Automatically scans and finds all Git repositories in specified directories
- 👤 **Author-Based Filtering** - Extract commits only from specific authors
- 📅 **Visual Date Picker** - Easy date selection with calendar widget and quick shortcuts
- 🎯 **Detailed & Summary Views** - Choose between detailed logs or concise summaries
- 🏷️ **Project Name Mapping** - Customize project names for better readability
- 🔄 **Auto-Pull Support** - Optionally pull latest changes before extraction
- 🌿 **Branch Control** - Extract from current branch or all branches
- 🖥️ **Material UI Design** - Modern, intuitive graphical interface
- 📦 **Portable Executable** - Standalone `.exe` file for Windows users
- ⚙️ **Template-Based Config** - Secure configuration management system

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
   - Use the visual date picker for date ranges

3. **Extract Logs**
   - Click "🚀 Start Extraction" and watch the magic happen!

#### Method 2: Command Line

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure**
   ```bash
   # Configuration file will be auto-created from template
   python gui.py
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

The tool uses a template-based configuration management system for security:

#### 📋 Configuration Structure
```
config.template.yaml  # Configuration template (version controlled)
config.yaml          # Personal config (auto-ignored)
```

#### 🔄 First-time Setup
The program automatically creates personal config from template:

```yaml
# Basic Configuration
root_directory: "C:\\workspace"          # Git repository root
author: "YourGitUsername"               # Git author name  
output_directory: "~/Desktop"           # Output directory

# Time Range (optional)
start_date: ""                          # Start date YYYY-MM-DD
end_date: ""                            # End date YYYY-MM-DD

# Output Options
detailed_output: true                   # Detailed logs
show_project_and_branch: true          # Show project/branch names

# Advanced Options
pull_latest_code: false                 # Pull before extraction
extract_all_branches: false            # Extract all branches

# Project Name Mapping
project_names:
  "my-project(master)": "My Project - "
  "api-service(develop)": "Backend API - "
```

#### 🔧 Configuration Management
- **Personal Config**: Edit `config.yaml` to set your paths and preferences
- **Config Updates**: Program automatically merges new configuration options
- **Backup & Restore**: Supports configuration backup and restore

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

## 中文

### 📖 项目简介

**Git 提交日志提取工具**是一款功能强大、使用便捷的开发者工具，专为自动化提取多个 Git 仓库的提交记录并生成工作日报而设计。无论是日常站会、工作汇报还是个人记录，这款工具都能让你轻松搞定！

### ✨ 核心特性

- 🔍 **智能仓库发现** - 自动扫描并找到指定目录下的所有 Git 仓库
- 👤 **作者筛选** - 按指定作者提取提交记录
- 📅 **可视化日期选择** - 日历控件选择日期，支持快捷日期设置
- 🎯 **详细&摘要视图** - 可选择详细日志或简洁摘要
- 🏷️ **项目名称映射** - 自定义项目名称，提高可读性
- 🔄 **自动拉取支持** - 可选择在提取前拉取最新代码
- 🌿 **分支控制** - 从当前分支或所有分支提取
- 🖥️ **Material UI设计** - 现代化直观的图形界面
- 📦 **便携执行文件** - Windows 用户可使用独立的 `.exe` 文件
- ⚙️ **模板化配置** - 安全的配置管理系统

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
   - 使用可视化日期选择器设置日期范围

3. **提取日志**
   - 点击 "🚀 开始提取日志" 按钮，见证奇迹发生！

#### 方式二：命令行

1. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

2. **配置设置**
   ```bash
   # 配置文件将从模板自动创建
   python gui.py
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

工具使用模板化配置管理系统，确保个人配置安全：

#### 📋 配置文件结构
```
config.template.yaml  # 配置模板（版本控制）
config.yaml          # 个人配置（自动忽略）
```

#### 🔄 首次配置
程序启动时会自动从模板创建个人配置文件：

```yaml
# 基本配置
root_directory: "C:\\workspace"          # Git仓库根目录
author: "你的Git用户名"                   # Git作者名
output_directory: "~/Desktop"           # 输出目录

# 时间范围（可选）
start_date: ""                          # 开始日期 YYYY-MM-DD
end_date: ""                            # 结束日期 YYYY-MM-DD

# 输出选项
detailed_output: true                   # 详细日志
show_project_and_branch: true          # 显示项目/分支名

# 高级选项
pull_latest_code: false                 # 提取前拉取代码
extract_all_branches: false            # 提取所有分支

# 项目名称映射
project_names:
  "my-project(master)": "我的项目-"
  "api-service(develop)": "后端API-"
```

#### 🔧 配置管理
- **个人配置**: 编辑 `config.yaml` 设置你的路径和偏好
- **配置更新**: 程序更新时会自动合并新的配置选项
- **备份恢复**: 支持配置文件备份和恢复

### 📋 输出示例

```
🎯 提交记录摘要 (2024-01-15):

我的项目-添加用户认证系统
我的项目-修复登录验证bug
后端API-实现新的REST接口
后端API-更新数据库架构
移动应用-增强UI响应性

📊 总计：3个项目共5次提交
⏱️ 生成时间：2024-01-15 18:30:22
```

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
