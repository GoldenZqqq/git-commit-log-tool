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


# config.yaml

# 根目录：指定要搜索的项目根目录

root_directory: "C:\\workspace"

# 提交作者：你希望过滤出提交记录的作者

author: "YourGitUsername"

# 输出目录：生成的工作日报将保存到该目录，默认是桌面

output_directory: "~/Desktop"

### 配置说明
root_directory: 指定要递归搜索 Git 仓库的根目录路径。可以是你在公司所有项目的根路径。
author: 你的 Git 用户名，用于筛选当天你的所有提交记录。
output_directory: 日报文件的保存路径，默认会保存在桌面上，但你也可以修改为其他路径。


### 使用说明

## 1. 运行脚本
   配置完成后，只需运行 main.py 脚本，工具将自动扫描指定根目录下的所有 Git 仓库，提取当日由配置文件中指定的作者所提交的记录。

```bash
python main.py
```

## 2. 查看工作日报
脚本运行结束后，工具将在你指定的输出目录中生成一个工作日报文件。文件名将以当天日期命名，格式如下：

```txt
git_commits_YYYY-MM-DD.txt
```
文件内容将包含每个项目的详细提交记录，包括提交哈希、作者、提交时间和提交信息，此外还会生成一个简洁的提交消息汇总，适用于日常工作汇报。

## 3. 示例输出
   生成的文件将如下所示：

```yaml
Repository: C:\workspace\project1
Hash: a1b2c3d4e5f6
Author: YourGitUsername
Date: 2024-10-14 12:34:56
Message: 修复登录问题

Repository: C:\workspace\project2
Hash: f6e5d4c3b2a1
Author: YourGitUsername
Date: 2024-10
Message: 修复注册问题
```
