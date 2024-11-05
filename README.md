# Git 提交日志提取工具 - 摸鱼神器

## 项目介绍

**Git 提交日志提取工具**是一款极其方便的工具，旨在帮助开发者自动化地从多个 Git 仓库中提取当日的所有提交记录，并生成当天的工作日报。这款工具非常适合在公司环境下工作，尤其是面对多个项目或多个 Git 仓库时，它能自动扫描并记录每个项目的 Git 提交历史，免去人工收集和整理的麻烦。

这款工具，堪称**摸鱼神器**：只需在下班前运行脚本，工具将自动生成一份包含当天工作内容的详细日报，让你能够轻松应对汇报工作进展的需求。再也不需要手动翻查每个项目的提交记录，只需运行一次脚本，所有信息将自动整理到一个文本文件中。

## 功能特性

- **自动化仓库扫描**：递归搜索指定目录下的所有 Git 仓库，无需手动指定每个仓库路径。
- **按作者筛选提交**：根据配置文件中设置的作者名，提取当天该作者的所有提交记录。
- **日报自动生成**：输出包含每个项目的详细提交记录及简洁的提交消息汇总，适用于日报汇报。
- **支持配置化**：只需修改配置文件中的少数参数，就可以适配不同的开发环境和需求。

## 安装说明

在开始使用之前，请确保你的系统中已经安装了 Python 3 和 `PyYAML` 库。如果尚未安装，可以按照以下步骤进行设置。

### 1. 克隆仓库

首先，克隆此项目的 Git 仓库到本地：

```bash
git clone https://github.com/your-username/git-commit-log-tool.git
cd git-commit-log-tool
```

### 2. 安装依赖

接下来，安装项目运行所需的依赖库。你可以使用 pip 安装 PyYAML，也可以直接通过 requirements.txt 文件安装所有依赖。

```bash
pip install -r requirements.txt
```

或直接安装 PyYAML：

```bash
pip install pyyaml
```

### 配置说明
```yaml
root_directory: "/path/to/repos"     # 必填，根目录，存放所有待扫描的 Git 仓库
author: "your-git-username"          # 必填，Git 提交者名称
output_directory: "/path/to/output"  # 可选，输出文件目录，默认输出到桌面
start_date: "2024-10-14"             # 可选，查询提交记录的起始日期，格式: YYYY-MM-DD
end_date: "2024-10-14"               # 可选，查询提交记录的结束日期，格式: YYYY-MM-DD
detailed_output: true                # 是否输出详细日志，默认为 true
show_project_and_branch: true        # 是否在最后的总结日志输出中列出每行的项目名与分支名，默认 true
pull_latest_code: false              # 是否在提取日志之前拉取最新代码，默认 false 
extract_all_branches: false          # 是否提取所有分支的提交记录，默认 false 只提取当前分支
project_names: false                 # 自定义项目名称吗，字典格式，格式为：项目名(分支名): "项目名称-"
```

### 使用说明

## 1. 运行脚本
   配置完成后，只需运行 main.py 脚本，工具将自动扫描指定根目录下的所有 Git 仓库，提取当日由配置文件中指定的作者所提交的记录。

```bash
python main.py
```

## 2. 脚本输出
脚本会递归查找 root_directory 下的所有 Git 仓库，获取指定作者的提交记录，并将其保存到指定的输出目录中。输出文件的文件名根据 start_date 和 end_date 动态生成，格式如下：

1.如果不填写 start_date 和 end_date，则默认为当天日期。
```txt
git_commits_YYYY-MM-DD.txt
```
2.如果填写了 start_date 和 end_date，则格式如下：

```txt
git_commits_YYYY-MM-DD_to_YYYY-MM-DD.txt
```
文件内容将包含每个项目的详细提交记录，包括提交哈希、作者、提交时间和提交信息，此外还会生成一个简洁的提交消息汇总，适用于日常工作汇报。

## 3. 示例输出
   生成的文件将如下所示：

```yaml
Repository: C:\workspace\project1
Hash: a1b2c3d4e5f6
Author: YourGitUsername
Date: 2024-10-14 12:34:56
Message: fix: 修复登录问题

Repository: C:\workspace\project2
Hash: f6e5d4c3b2a1
Author: YourGitUsername
Date: 2024-10-14 23:45:23
Message: feat: 增加第三方用户登录页面

========================================
Summary of all commit messages:

project1 - 若依后台管理系统-修复登录问题
project2 - 若依商城用户端H5-增加第三方用户登录页面
```
### 扩展功能
未来可能扩展的功能包括：

- **自动拉取项目所在分支最新代码后再进行日志提取。**
- **支持通过命令行参数指定时间范围，覆盖 config.yaml 中的设置。**
- **增加其他筛选条件，例如按提交消息关键字过滤。**
- **提供更灵活的输出格式，如 JSON 或 CSV 格式的输出文件。**


### 贡献
欢迎提交 Pull Request 以改进此工具，或者报告问题与建议！

### 许可证
MIT License