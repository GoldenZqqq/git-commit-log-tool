# 🚀 Git 提交日志提取工具 - 详细使用指南

## 📋 目录
- [快速开始](#快速开始)
- [GUI界面使用](#gui界面使用)
- [命令行使用](#命令行使用)
- [配置详解](#配置详解)
- [高级功能](#高级功能)
- [故障排除](#故障排除)
- [最佳实践](#最佳实践)

## 🚀 快速开始

### 方式一：使用可执行文件（推荐）
1. 下载 `GitCommitTool.exe`
2. 双击运行，无需安装Python
3. 配置参数后点击"开始提取日志"

### 方式二：Python环境运行
1. 确保Python 3.7+已安装
2. 克隆或下载项目
3. 运行 `start.bat`（Windows）或 `python gui.py`

## 🖥️ GUI界面使用

### 主界面布局
```
┌─────────────────────────────────────────┐
│  🚀 Git 提交日志提取工具                │
├─────────────────────────────────────────┤
│  基本配置                               │
│  ├─ 根目录: [浏览] C:\workspace         │
│  ├─ 作者名: YourGitUsername             │
│  ├─ 输出目录: [浏览] C:\Output          │
│  ├─ 开始日期: 2024-01-01 (可选)        │
│  └─ 结束日期: 2024-01-31 (可选)        │
├─────────────────────────────────────────┤
│  高级选项                               │
│  ☑ 输出详细日志                        │
│  ☑ 显示项目名与分支名                  │
│  ☐ 提取前拉取最新代码                  │
│  ☐ 提取所有分支的提交记录              │
├─────────────────────────────────────────┤
│  项目名称映射 (可选)                    │
│  my-project(master) -> 我的项目-        │
│  api-service(dev) -> 后端API-           │
├─────────────────────────────────────────┤
│  [💾 保存配置] [📂 重新加载] [🚀 开始]   │
│  ████████████ 50% 处理中...             │
├─────────────────────────────────────────┤
│  运行日志                               │
│  [18:30:22] 🔍 开始搜索Git仓库...       │
│  [18:30:23] ✅ 找到 5 个Git仓库         │
│  [18:30:24] 📂 处理仓库 1/5: my-project │
└─────────────────────────────────────────┘
```

### 配置步骤详解

#### 1. 基本配置
- **根目录**: 选择包含所有Git仓库的父目录
  - 示例: `C:\workspace` 或 `/home/user/projects`
  - 工具会递归扫描所有子目录中的Git仓库

- **作者名**: 输入你的Git用户名
  - 必须与Git配置中的 `user.name` 一致
  - 可通过 `git config user.name` 查看

- **输出目录**: 选择日志文件保存位置
  - 建议选择桌面或专门的文档文件夹
  - 确保目录有写入权限

- **日期范围**: 可选的时间筛选
  - 格式: `YYYY-MM-DD`
  - 留空则默认为当天
  - 支持跨月、跨年查询

#### 2. 高级选项
- **输出详细日志**: 包含完整的提交信息（哈希、时间等）
- **显示项目名与分支名**: 在摘要中显示项目和分支信息
- **提取前拉取最新代码**: 自动执行 `git pull` 获取最新提交
- **提取所有分支**: 不仅限于当前分支，包含所有分支的提交

#### 3. 项目名称映射
自定义项目显示名称，格式：
```
原项目名(分支名) -> 自定义名称
```
示例：
```
ecommerce-api(master) -> 电商后端API-
mobile-app(develop) -> 移动应用-
admin-panel(*) -> 管理后台-  # 通配符匹配所有分支
```

### 操作流程
1. **配置参数** → 填写必要的配置信息
2. **保存配置** → 将设置保存到config.yaml（可选）
3. **开始提取** → 点击按钮开始处理
4. **查看日志** → 实时查看处理进度和结果
5. **打开文件** → 完成后可选择直接打开生成的文件

## 💻 命令行使用

### 基本命令
```bash
# 使用默认配置
python main.py

# 指定配置文件
python main.py --config custom_config.yaml
```

### 配置文件路径
- 默认: `config.yaml`
- 自定义: 通过 `--config` 参数指定

## ⚙️ 配置详解

### 完整配置示例
```yaml
# 基本设置
root_directory: "C:\\workspace"
author: "YourGitUsername"
output_directory: "C:\\Users\\You\\Desktop"

# 时间范围
start_date: "2024-01-01"  # 可选，格式: YYYY-MM-DD
end_date: "2024-01-31"    # 可选，格式: YYYY-MM-DD

# 输出控制
detailed_output: true             # 详细日志
show_project_and_branch: true    # 显示项目/分支

# 仓库操作
pull_latest_code: false          # 拉取最新代码
extract_all_branches: false      # 所有分支

# 项目名称映射
project_names:
  # 精确匹配: 项目名(分支名)
  "my-api(master)": "生产API-"
  "my-api(develop)": "开发API-"
  
  # 通配符匹配: 项目名(*)
  "frontend(*)": "前端项目-"
  
  # 完全自定义
  "legacy-system(main)": "遗留系统维护-"
```

### 配置项说明

| 配置项 | 类型 | 必填 | 默认值 | 说明 |
|--------|------|------|--------|------|
| `root_directory` | string | ✅ | 无 | Git仓库根目录 |
| `author` | string | ✅ | 无 | Git作者名 |
| `output_directory` | string | ✅ | 无 | 输出目录 |
| `start_date` | string | ❌ | 今天 | 开始日期 |
| `end_date` | string | ❌ | 今天 | 结束日期 |
| `detailed_output` | boolean | ❌ | true | 详细输出 |
| `show_project_and_branch` | boolean | ❌ | true | 显示项目/分支 |
| `pull_latest_code` | boolean | ❌ | false | 拉取最新代码 |
| `extract_all_branches` | boolean | ❌ | false | 所有分支 |
| `project_names` | object | ❌ | {} | 项目名映射 |

## 🔧 高级功能

### 自动拉取最新代码
启用 `pull_latest_code` 后，工具会在提取前为每个仓库执行：
```bash
git pull
```
注意：
- 需要确保仓库没有未提交的更改
- 需要有相应的拉取权限
- 可能会影响提取速度

### 多分支提取
启用 `extract_all_branches` 后，使用以下命令：
```bash
git log --all --since="..." --until="..." --author="..."
```
适用场景：
- 需要查看所有分支的工作
- 跨分支开发的项目
- 完整的提交历史分析

### 项目名称映射规则
1. **精确匹配**: `项目名(分支名)` → 完全匹配项目和分支
2. **通配符匹配**: `项目名(*)` → 匹配项目的所有分支
3. **优先级**: 精确匹配 > 通配符匹配 > 默认名称

### 批量处理
对于大量仓库的场景：
1. 使用SSD存储以提高扫描速度
2. 避免网络驱动器
3. 考虑使用多线程（未来版本）

## 🔍 故障排除

### 常见问题

#### 1. 未找到Git仓库
**现象**: "找到 0 个Git仓库"
**原因**: 
- 路径错误
- 没有.git目录
- 权限不足

**解决**:
```bash
# 检查目录结构
ls -la /path/to/repos/
# 或 Windows
dir C:\workspace /s /b | findstr "\.git"
```

#### 2. 无提交记录
**现象**: "未找到任何提交记录"
**原因**:
- 作者名不匹配
- 日期范围外
- 分支没有提交

**解决**:
```bash
# 检查Git配置
git config user.name

# 检查最近提交
git log --oneline -10

# 检查作者提交
git log --author="YourName" --since="1 week ago"
```

#### 3. 权限错误
**现象**: 无法写入输出文件
**解决**:
- 选择有写入权限的目录
- 以管理员身份运行
- 检查磁盘空间

#### 4. 编码问题
**现象**: 中文乱码
**解决**:
- 确保 `git config core.quotepath false`
- 使用UTF-8编码
- Windows用户设置环境变量 `PYTHONIOENCODING=utf-8`

### 调试模式
在GUI的日志区域可以看到详细的执行过程：
- 🔍 搜索阶段
- 📂 处理阶段  
- ✅ 成功状态
- ❌ 错误信息

## 💡 最佳实践

### 1. 目录组织
推荐的工作目录结构：
```
workspace/
├── project1/           # Git仓库1
│   └── .git/
├── project2/           # Git仓库2  
│   └── .git/
├── client-projects/    # 客户项目
│   ├── client-a/
│   └── client-b/
└── personal/          # 个人项目
    ├── tool1/
    └── tool2/
```

### 2. 作者名统一
确保所有仓库使用相同的作者名：
```bash
# 全局设置
git config --global user.name "YourName"

# 检查现有仓库
find . -name ".git" -type d | while read dir; do
    cd "$dir/.."
    echo "=== $(pwd) ==="
    git config user.name
    cd - > /dev/null
done
```

### 3. 定期备份配置
```bash
# 备份配置
cp config.yaml config_backup.yaml

# 版本控制配置模板
git add config.template.yaml
```

### 4. 输出文件管理
- 使用有意义的文件名
- 定期清理旧文件
- 考虑按月份归档

### 5. 性能优化
- 避免扫描过深的目录
- 排除不必要的子目录
- 使用.gitignore避免扫描临时文件

## 📊 输出格式示例

### 详细模式输出
```
Repository: C:\workspace\my-project
Hash: a1b2c3d4e5f6g7h8i9j0
Author: YourName
Date: 2024-01-15 14:30:25 +0800
Message: feat: 添加用户认证功能

实现了JWT token认证
- 添加登录/登出接口
- 实现权限验证中间件
- 更新用户模型

========================================

Repository: C:\workspace\api-service
Hash: b2c3d4e5f6g7h8i9j0k1
Author: YourName  
Date: 2024-01-15 16:45:10 +0800
Message: fix: 修复数据库连接池配置

========================================
Summary of all commit messages:

my-project(master) - 生产系统-添加用户认证功能
api-service(develop) - 后端API-修复数据库连接池配置
```

### 简洁模式输出
```
🎯 提交记录摘要 (2024-01-15):

生产系统-添加用户认证功能
后端API-修复数据库连接池配置  
移动应用-优化界面响应性能
管理后台-增加数据导出功能

📊 总计：4个项目共4次提交
⏱️ 生成时间：2024-01-15 18:30:22
```

---

如有其他问题，请查看项目的 [Issues](https://github.com/yourusername/git-commit-log-tool/issues) 或创建新的问题报告。 