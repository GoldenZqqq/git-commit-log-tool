# Contributing to Git Commit Log Extractor

感谢你对 Git 提交日志提取工具的贡献兴趣！ 🎉

我们欢迎各种形式的贡献，包括但不限于：

## 🤝 贡献方式

### 🐛 报告Bug
- 使用清晰、描述性的标题
- 详细描述复现步骤
- 包含错误截图（如果适用）
- 说明预期行为和实际行为
- 提供环境信息（操作系统、Python版本等）

### 💡 功能建议
- 使用清晰、描述性的标题
- 详细说明功能的用途和价值
- 如果可能，提供使用场景示例
- 考虑功能的可行性和维护成本

### 🔧 代码贡献

#### 开发环境设置
1. Fork 本仓库
2. 克隆你的 fork
   ```bash
   git clone https://github.com/YOUR_USERNAME/git-commit-log-tool.git
   cd git-commit-log-tool
   ```
3. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```
4. 创建新分支
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### 代码规范
- 使用 Python PEP 8 代码风格
- 添加适当的注释和文档字符串
- 为新功能编写测试
- 确保所有测试通过

#### 提交规范
使用语义化提交信息：
```
feat: 添加新功能
fix: 修复bug
docs: 更新文档
style: 代码格式调整
refactor: 重构代码
test: 添加测试
chore: 构建过程或辅助工具变动
```

#### Pull Request 流程
1. 确保你的代码符合项目标准
2. 更新相关文档
3. 添加或更新测试
4. 确保所有检查通过
5. 创建 Pull Request，包含：
   - 清晰的标题和描述
   - 变更列表
   - 相关的 issue 引用
   - 测试说明

## 📋 开发指南

### 项目结构
```
git-commit-log-tool/
├── gui.py                 # GUI界面主文件
├── git_commit_tool.py     # 核心功能模块
├── main.py               # 命令行入口
├── build.py              # 打包脚本
├── config.yaml           # 配置文件
├── requirements.txt      # 依赖列表
├── README.md            # 项目说明
└── tests/               # 测试文件
```

### 核心模块说明

#### `git_commit_tool.py`
- `find_git_repos()`: 递归查找Git仓库
- `get_git_commits()`: 获取提交记录
- `save_commits_to_file()`: 保存结果到文件
- `load_config()`: 加载配置文件

#### `gui.py`
- `GitCommitToolGUI`: 主GUI类
- 使用 tkinter 构建界面
- 支持配置管理和实时日志

### 测试指南
```bash
# 运行所有测试
python -m pytest tests/

# 运行特定测试文件
python -m pytest tests/test_git_commit_tool.py

# 生成覆盖率报告
python -m pytest --cov=. tests/
```

## 🏷️ 发布流程

### 版本号规范
使用语义化版本号：`MAJOR.MINOR.PATCH`
- MAJOR: 不兼容的 API 修改
- MINOR: 向下兼容的功能性新增
- PATCH: 向下兼容的问题修正

### 发布步骤
1. 更新版本号
2. 更新 CHANGELOG.md
3. 创建 release tag
4. 构建和测试可执行文件
5. 发布到 GitHub Releases

## 📝 文档贡献

### README 更新
- 保持中英文同步
- 更新功能列表和截图
- 确保示例代码可运行

### 代码文档
- 为所有公共函数添加文档字符串
- 使用清晰的变量和函数命名
- 添加内联注释解释复杂逻辑

## 🛡️ 安全考虑

- 不要在代码中硬编码敏感信息
- 验证用户输入
- 安全处理文件路径
- 注意 Git 命令注入风险

## 📞 获取帮助

- 创建 Issue 讨论功能或报告问题
- 查看现有的 Issue 和 Pull Request
- 参考项目 Wiki（如果有）

## 📜 许可证

通过向本项目贡献，你同意你的贡献将在 MIT 许可证下授权。

---

再次感谢你的贡献！让我们一起让这个工具变得更好！ 🚀 