#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Git提交日志提取工具 - 功能演示脚本
展示工具的核心功能，无需GUI界面
"""

import os
import sys
import datetime
from git_commit_tool import find_git_repos, get_git_commits, save_commits_to_file, load_config

def demo_basic_functionality():
    """演示基本功能"""
    print("🚀 Git提交日志提取工具 - 功能演示")
    print("=" * 50)
    
    # 检查当前目录是否为Git仓库
    if os.path.exists('.git'):
        print("✅ 检测到当前目录是Git仓库")
        demo_current_repo()
    else:
        print("⚠️ 当前目录不是Git仓库，演示仓库搜索功能")
        demo_repo_search()

def demo_current_repo():
    """演示当前仓库的提交提取"""
    print("\n🔍 演示：提取当前仓库的提交记录")
    
    # 获取当前用户的Git配置
    try:
        import subprocess
        result = subprocess.run(['git', 'config', 'user.name'], 
                              capture_output=True, text=True, check=True)
        author = result.stdout.strip()
        print(f"📝 检测到Git作者: {author}")
    except:
        author = "Demo User"
        print("⚠️ 无法获取Git配置，使用演示作者名")
    
    # 获取最近几天的提交
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    week_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    
    print(f"📅 查询日期范围: {week_ago} 到 {today}")
    
    try:
        commits, messages = get_git_commits(
            repo_path=os.getcwd(),
            start_date=week_ago,
            end_date=today,
            author=author,
            pull_latest_code=False,
            extract_all_branches=False
        )
        
        if commits:
            print(f"✅ 找到 {len(commits)} 个提交记录")
            
            # 显示前3个提交的摘要
            print("\n📋 提交摘要（最多显示3个）:")
            for i, (repo_path, message) in enumerate(messages[:3], 1):
                print(f"  {i}. {message[:80]}...")
            
            # 保存到演示文件
            demo_output = f"demo_commits_{today}.txt"
            save_commits_to_file(
                commits, messages, demo_output,
                detailed_output=True,
                project_names={"git-commit-log-tool(*)": "摸鱼神器-"},
                show_project_and_branch=True
            )
            print(f"💾 演示文件已保存: {demo_output}")
            
        else:
            print("📭 未找到匹配的提交记录")
            print("💡 提示: 尝试修改作者名或扩大日期范围")
            
    except Exception as e:
        print(f"❌ 演示过程中发生错误: {e}")

def demo_repo_search():
    """演示仓库搜索功能"""
    print("\n🔍 演示：搜索Git仓库")
    
    # 搜索当前目录下的Git仓库
    current_dir = os.getcwd()
    repos = find_git_repos(current_dir)
    
    if repos:
        print(f"✅ 在 {current_dir} 下找到 {len(repos)} 个Git仓库:")
        for i, repo in enumerate(repos[:5], 1):  # 最多显示5个
            print(f"  {i}. {repo}")
        
        if len(repos) > 5:
            print(f"  ... 还有 {len(repos) - 5} 个仓库")
    else:
        print(f"📭 在 {current_dir} 下未找到Git仓库")
        print("💡 提示: 请在包含Git仓库的目录中运行演示")

def demo_config_loading():
    """演示配置加载功能"""
    print("\n⚙️ 演示：配置文件加载")
    
    try:
        config = load_config()
        print("✅ 成功加载配置文件:")
        
        key_configs = [
            'root_directory', 'author', 'output_directory',
            'detailed_output', 'show_project_and_branch'
        ]
        
        for key in key_configs:
            value = config.get(key, '未设置')
            print(f"  📌 {key}: {value}")
            
    except Exception as e:
        print(f"❌ 配置加载失败: {e}")
        print("💡 提示: 请确保 config.yaml 文件存在且格式正确")

def demo_gui_info():
    """展示GUI使用信息"""
    print("\n🖥️ GUI界面使用说明")
    print("-" * 30)
    print("🚀 启动GUI:")
    print("  方式1: 双击 start.bat (Windows)")
    print("  方式2: python gui.py")
    print("  方式3: 使用打包好的 GitCommitTool.exe")
    
    print("\n📦 打包为exe:")
    print("  python build.py")
    
    print("\n🎯 主要功能:")
    print("  ✨ 可视化配置界面")
    print("  🔍 实时仓库扫描")
    print("  📊 进度显示")
    print("  📝 实时日志输出")
    print("  💾 配置自动保存")

def main():
    """主演示函数"""
    try:
        demo_basic_functionality()
        demo_config_loading()
        demo_gui_info()
        
        print("\n" + "=" * 50)
        print("🎉 演示完成!")
        print("📖 更多信息请查看:")
        print("  📋 README.md - 项目说明")
        print("  📚 USAGE.md - 详细使用指南")
        print("  🤝 CONTRIBUTING.md - 贡献指南")
        print("\n💫 享受摸鱼的快乐时光！")
        
    except KeyboardInterrupt:
        print("\n⚠️ 演示被用户中断")
    except Exception as e:
        print(f"\n❌ 演示过程中发生未预期的错误: {e}")
        print("💡 请检查环境配置或联系开发者")

if __name__ == "__main__":
    main() 