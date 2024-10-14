from git_commit_tool import find_git_repos, get_git_commits_for_day_in_repo, save_commits_to_file, load_config
import os
import datetime

if __name__ == "__main__":
    # 加载配置
    config = load_config()

    # 从配置文件中获取变量
    root_directory = config.get('root_directory', 'C:\\workspace')
    author = config.get('author', 'YourName')
    output_directory = config.get('output_directory', '~/Desktop')

    # 获取当前日期
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    # 查找所有 git 仓库
    git_repos = find_git_repos(root_directory)
    all_commits = []
    all_messages = []

    # 遍历每个仓库，获取提交记录
    for repo in git_repos:
        commits, messages = get_git_commits_for_day_in_repo(repo, today, author)
        if commits:
            all_commits.extend(commits)
            all_messages.extend(messages)

    # 保存提交记录到指定文件夹
    output_file = os.path.join(os.path.expanduser(output_directory), f"git_commits_{today}.txt")
    
    if all_commits:
        save_commits_to_file(all_commits, all_messages, output_file)
    else:
        print(f"No commits found for {today}")
