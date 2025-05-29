# 📝 Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- [ ] 多线程处理以提高大量仓库的处理速度
- [ ] 支持自定义输出格式 (JSON, CSV, HTML)
- [ ] 添加提交统计分析功能
- [ ] 支持远程仓库提取
- [ ] 添加定时任务功能
- [ ] 支持Git Hook集成

## [1.0.0] - 2024-12-XX

### 🎉 Initial Release

#### Added
- ✨ **完整的GUI界面** - 基于tkinter的现代化界面
  - 直观的配置面板
  - 实时进度显示
  - 详细的运行日志
  - 自动配置保存/加载

- 🔍 **智能仓库发现** - 递归扫描指定目录下的所有Git仓库
  - 自动识别.git目录
  - 支持多级目录扫描
  - 智能过滤非Git目录

- 👤 **灵活的作者筛选** - 按指定作者提取提交记录
  - 支持精确匹配
  - 大小写敏感
  - 支持中文作者名

- 📅 **强大的日期范围支持**
  - 单日提取（默认今天）
  - 自定义日期范围
  - 跨月跨年支持
  - YYYY-MM-DD格式

- 🎯 **双重输出模式**
  - **详细模式**: 包含完整提交信息（哈希、时间、完整消息）
  - **摘要模式**: 简洁的提交消息列表，适合日报

- 🏷️ **项目名称映射系统**
  - 支持精确匹配: `project(branch)`
  - 支持通配符: `project(*)`
  - 自定义显示名称
  - 优先级匹配规则

- 🔄 **高级Git操作**
  - 可选的自动拉取最新代码
  - 支持所有分支提取
  - 当前分支检测
  - 安全的Git命令执行

- 📦 **便携版支持**
  - PyInstaller打包为独立exe
  - 无需Python环境
  - 包含所有依赖
  - 一键式部署

- ⚙️ **完善的配置管理**
  - YAML格式配置文件
  - GUI配置同步
  - 配置验证
  - 默认值处理

- 🖥️ **跨平台兼容**
  - Windows (主要支持)
  - macOS (基本支持)
  - Linux (基本支持)

#### Technical Features
- 🎨 **现代化UI设计**
  - 深色主题
  - 图标按钮
  - 进度指示器
  - 滚动支持

- 🧵 **多线程架构**
  - GUI响应性
  - 后台处理
  - 实时日志更新
  - 安全的线程通信

- 🛡️ **错误处理机制**
  - 全面的异常捕获
  - 用户友好的错误消息
  - 详细的调试信息
  - 优雅的失败处理

- 📁 **智能文件管理**
  - 自动文件名生成
  - 路径规范化
  - 权限检查
  - 覆盖保护

#### File Structure
```
git-commit-log-tool/
├── gui.py                 # 🖥️ GUI主界面
├── git_commit_tool.py     # 🔧 核心功能模块  
├── main.py               # 💻 命令行入口
├── build.py              # 📦 自动打包脚本
├── start.bat             # 🚀 Windows快速启动
├── config.yaml           # ⚙️ 配置文件
├── requirements.txt      # 📋 依赖列表
├── README.md            # 📖 项目说明 (中英文)
├── USAGE.md             # 📚 详细使用指南
├── CONTRIBUTING.md      # 🤝 贡献指南
├── CHANGELOG.md         # 📝 更新日志
├── LICENSE              # 📄 开源许可证
└── .gitignore           # 🚫 Git忽略规则
```

#### Supported Output Formats
- 📄 **纯文本格式** (.txt)
  - UTF-8编码
  - 中文支持
  - 结构化布局

#### Configuration Options
- 🎛️ **基本配置**
  - `root_directory`: 扫描根目录
  - `author`: Git作者名
  - `output_directory`: 输出目录
  - `start_date`: 开始日期 (可选)
  - `end_date`: 结束日期 (可选)

- 🔧 **高级选项**
  - `detailed_output`: 详细输出模式
  - `show_project_and_branch`: 显示项目/分支信息
  - `pull_latest_code`: 提取前拉取最新代码
  - `extract_all_branches`: 提取所有分支

- 🏷️ **项目映射**
  - `project_names`: 项目名称自定义映射

#### Known Limitations
- 需要本地Git仓库访问权限
- 依赖Git命令行工具
- 大量仓库处理可能较慢
- 网络驱动器性能影响

#### Minimum Requirements
- Python 3.7+ (源码运行)
- Git 2.0+ (命令行工具)
- Windows 10+ (exe版本)
- 50MB 磁盘空间

---

## Version History

### Pre-release Versions

#### [0.3.0] - 2024-XX-XX
- 🎨 添加GUI界面原型
- 🔧 重构核心模块
- 📖 完善文档

#### [0.2.0] - 2024-XX-XX  
- 🏷️ 添加项目名称映射
- 🌿 支持多分支提取
- 🔄 添加自动拉取功能

#### [0.1.0] - 2024-XX-XX
- 🎯 基础命令行版本
- 📅 日期范围支持
- 👤 作者筛选功能

---

## 🎯 Future Roadmap

### v1.1.0 (计划)
- 📊 **提交统计分析**
  - 每日提交数量统计
  - 代码行数变化
  - 项目活跃度分析
  - 图表生成

- 🌐 **输出格式扩展**
  - JSON格式导出
  - CSV格式导出  
  - HTML网页报告
  - Markdown格式

### v1.2.0 (计划)
- ⚡ **性能优化**
  - 多线程仓库处理
  - 缓存机制
  - 增量更新
  - 进度百分比

- 🔌 **集成功能**
  - Git Hook集成
  - CI/CD支持
  - 定时任务
  - 邮件发送

### v2.0.0 (远期)
- ☁️ **云服务支持**
  - GitHub API集成
  - GitLab API集成
  - 远程仓库访问
  - OAuth认证

- 🎨 **界面升级**
  - Web界面
  - 现代化设计
  - 响应式布局
  - 主题切换

---

**Made with ❤️ by developers, for developers**

> *让每一次提交都有价值，让每一份工作都被记录！* 