import os
import datetime
import subprocess
import yaml  # 用来读取 YAML 配置文件
import re

def load_config(config_file="config.yaml"):
    """
    从配置文件中加载配置项。
    
    :param config_file: 配置文件路径
    :return: 配置项的字典
    """
    with open(config_file, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


def find_git_repos(root_dir, max_depth=None):
    """
    递归查找 root_dir 下的所有 git 仓库。
    :param root_dir: 搜索的根目录
    :param max_depth: 最大递归深度，如果为 None 则不限制
    :return: 包含所有 Git 仓库路径的列表
    """
    git_repos = []

    for root, dirs, files in os.walk(root_dir):
        if max_depth is not None:
            current_depth = len(os.path.relpath(root, root_dir).split(os.sep))
            if current_depth > max_depth:
                dirs[:] = []  # 防止进一步递归
                continue

        if '.git' in dirs:  # 如果找到 .git 目录，认为是 Git 仓库
            git_repos.append(root)
            dirs[:] = []  # 防止递归进入子目录

    return git_repos
        
def get_current_branch(repo_path):
    """获取当前Git分支名称"""
    try:
        os.chdir(repo_path)  # 切换到指定的仓库路径
        return subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        return "unknown branch"


def get_git_commits(repo_path, start_date, end_date, author):
    """
    获取指定日期、作者的 git 提交记录。

    :param repo_path: 仓库路径
    :param date_str: 日期字符串，格式为 'YYYY-MM-DD'
    :param author: 作者名
    :return: 提交记录和提交信息列表
    """
    try:
        os.chdir(repo_path)

        git_log_command = [
            'git', 'log',
            '--since="{} 00:00:00"'.format(start_date),
            '--until="{} 23:59:59"'.format(end_date),
            '--author={}'.format(author),
            '--pretty=format:Hash: %H%nAuthor: %an%nDate: %ad%nMessage: %B%n',
            '--date=iso'
        ]
        result = subprocess.run(git_log_command, capture_output=True, text=True, check=True, encoding='utf-8')

        if result.stdout is None:
            print(f"Error: No output from git log in {repo_path}")
            return [], []
        
        commits = []
        messages = []

        for commit in result.stdout.strip().split('\n\n'):
            if commit:
                cleaned_commit = f"Repository: {repo_path}\n{commit.strip()}"
                commits.append(cleaned_commit)

                message_start = commit.find('Message:')
                if message_start != -1:
                    message = commit[message_start + len('Message:'):].strip()
                    messages.append((repo_path, message))

        return commits, messages
    
    except subprocess.CalledProcessError as e:
        print(f"Error in {repo_path}: {e}")
        return [], []


def clean_commit_message(message):
    """
    去掉 'feat: ', 'fix: ' 等前缀，并处理任何特殊符号。
    
    :param message: 原始提交信息
    :return: 处理后的提交信息
    """
    cleaned_message = re.sub(r'^(feat|fix|refactor|chore|docs|style|test|perf|ci|build|revert):\s*', '', message, flags=re.IGNORECASE)
    cleaned_message = cleaned_message.replace("['']", "").replace('"', '')
    return cleaned_message


def save_commits_to_file(commits, messages, output_file, detailed_output):
    """
    将所有仓库的 commit 记录保存到指定文件，并在文件末尾汇总所有的提交 message。
    
    :param commits: commit 记录列表。
    :param messages: 所有 commit 的 message 列表（包含 repo 路径信息）。
    :param output_file: 输出文件路径。
    :param detailed_output: 布尔值，控制是否输出详细记录。
    """
    try:
        output_file = os.path.abspath(output_file)

        with open(output_file, 'w', encoding='utf-8') as f:
            if detailed_output:
                for commit in commits:
                    f.write(commit + '\n\n')
                    f.write('\n' + '='*40 + '\n')
                    f.write('Summary of all commit messages:\n\n')
            
            for entry in messages:
                if isinstance(entry, tuple) and len(entry) == 2:
                    repo_path, message = entry
                    project_name = os.path.basename(repo_path)
                    cleaned_message = clean_commit_message(message)
                    
                    # 获取当前分支名称
                    current_branch = get_current_branch(repo_path)
                    f.write(f"{project_name}({current_branch}) - {cleaned_message}\n")
                    
        
        print(f"File successfully saved at: {output_file}")
    except Exception as e:
        print(f"Failed to save file: {e}")
