import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import datetime
import json
import threading
from git_commit_tool import find_git_repos, get_git_commits, save_commits_to_file, load_config
import yaml

class GitCommitToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Git 提交日志提取工具 - 摸鱼神器 v1.0")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # 设置主题颜色
        self.bg_color = "#2c3e50"
        self.accent_color = "#3498db"
        self.success_color = "#2ecc71"
        self.warning_color = "#f39c12"
        
        self.root.configure(bg=self.bg_color)
        
        # 创建样式
        self.setup_styles()
        
        # 创建主框架
        self.create_main_frame()
        
        # 加载配置
        self.load_config_to_gui()
    
    def setup_styles(self):
        """设置GUI样式"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # 配置样式
        style.configure('Title.TLabel', 
                       background=self.bg_color, 
                       foreground='white', 
                       font=('Arial', 16, 'bold'))
        
        style.configure('Heading.TLabel', 
                       background=self.bg_color, 
                       foreground='white', 
                       font=('Arial', 12, 'bold'))
        
        style.configure('Custom.TFrame', 
                       background=self.bg_color)
        
        style.configure('Custom.TButton', 
                       background=self.accent_color, 
                       foreground='white',
                       font=('Arial', 10, 'bold'))
        
        style.map('Custom.TButton',
                 background=[('active', '#2980b9')])
    
    def create_main_frame(self):
        """创建主界面框架"""
        # 创建滚动框架
        self.canvas = tk.Canvas(self.root, bg=self.bg_color, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas, style='Custom.TFrame')
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        self.scrollbar.pack(side="right", fill="y")
        
        # 标题
        title_label = ttk.Label(self.scrollable_frame, 
                              text="🚀 Git 提交日志提取工具", 
                              style='Title.TLabel')
        title_label.pack(pady=(0, 20))
        
        # 创建配置区域
        self.create_config_section()
        
        # 创建高级选项区域
        self.create_advanced_section()
        
        # 创建项目名称映射区域
        self.create_project_names_section()
        
        # 创建操作按钮区域
        self.create_action_section()
        
        # 创建日志输出区域
        self.create_log_section()
    
    def create_config_section(self):
        """创建基本配置区域"""
        config_frame = ttk.LabelFrame(self.scrollable_frame, text="基本配置", padding=10)
        config_frame.pack(fill="x", pady=(0, 10))
        
        # 根目录选择
        ttk.Label(config_frame, text="根目录:").grid(row=0, column=0, sticky="w", pady=5)
        self.root_dir_var = tk.StringVar()
        root_dir_frame = ttk.Frame(config_frame)
        root_dir_frame.grid(row=0, column=1, sticky="ew", pady=5, columnspan=2)
        
        self.root_dir_entry = ttk.Entry(root_dir_frame, textvariable=self.root_dir_var, width=50)
        self.root_dir_entry.pack(side="left", fill="x", expand=True)
        
        ttk.Button(root_dir_frame, text="浏览", 
                  command=self.browse_root_directory).pack(side="right", padx=(5, 0))
        
        # 作者名
        ttk.Label(config_frame, text="作者名:").grid(row=1, column=0, sticky="w", pady=5)
        self.author_var = tk.StringVar()
        ttk.Entry(config_frame, textvariable=self.author_var, width=30).grid(row=1, column=1, sticky="w", pady=5)
        
        # 输出目录选择
        ttk.Label(config_frame, text="输出目录:").grid(row=2, column=0, sticky="w", pady=5)
        self.output_dir_var = tk.StringVar()
        output_dir_frame = ttk.Frame(config_frame)
        output_dir_frame.grid(row=2, column=1, sticky="ew", pady=5, columnspan=2)
        
        self.output_dir_entry = ttk.Entry(output_dir_frame, textvariable=self.output_dir_var, width=50)
        self.output_dir_entry.pack(side="left", fill="x", expand=True)
        
        ttk.Button(output_dir_frame, text="浏览", 
                  command=self.browse_output_directory).pack(side="right", padx=(5, 0))
        
        # 日期选择
        ttk.Label(config_frame, text="开始日期:").grid(row=3, column=0, sticky="w", pady=5)
        self.start_date_var = tk.StringVar()
        ttk.Entry(config_frame, textvariable=self.start_date_var, width=15).grid(row=3, column=1, sticky="w", pady=5)
        ttk.Label(config_frame, text="(YYYY-MM-DD，留空为今天)").grid(row=3, column=2, sticky="w", pady=5)
        
        ttk.Label(config_frame, text="结束日期:").grid(row=4, column=0, sticky="w", pady=5)
        self.end_date_var = tk.StringVar()
        ttk.Entry(config_frame, textvariable=self.end_date_var, width=15).grid(row=4, column=1, sticky="w", pady=5)
        ttk.Label(config_frame, text="(YYYY-MM-DD，留空为今天)").grid(row=4, column=2, sticky="w", pady=5)
        
        # 配置grid权重
        config_frame.columnconfigure(1, weight=1)
    
    def create_advanced_section(self):
        """创建高级选项区域"""
        advanced_frame = ttk.LabelFrame(self.scrollable_frame, text="高级选项", padding=10)
        advanced_frame.pack(fill="x", pady=(0, 10))
        
        # 详细输出
        self.detailed_output_var = tk.BooleanVar()
        ttk.Checkbutton(advanced_frame, text="输出详细日志", 
                       variable=self.detailed_output_var).grid(row=0, column=0, sticky="w", pady=2)
        
        # 显示项目和分支
        self.show_project_branch_var = tk.BooleanVar()
        ttk.Checkbutton(advanced_frame, text="显示项目名与分支名", 
                       variable=self.show_project_branch_var).grid(row=0, column=1, sticky="w", pady=2)
        
        # 拉取最新代码
        self.pull_latest_var = tk.BooleanVar()
        ttk.Checkbutton(advanced_frame, text="提取前拉取最新代码", 
                       variable=self.pull_latest_var).grid(row=1, column=0, sticky="w", pady=2)
        
        # 提取所有分支
        self.extract_all_branches_var = tk.BooleanVar()
        ttk.Checkbutton(advanced_frame, text="提取所有分支的提交记录", 
                       variable=self.extract_all_branches_var).grid(row=1, column=1, sticky="w", pady=2)
    
    def create_project_names_section(self):
        """创建项目名称映射区域"""
        project_frame = ttk.LabelFrame(self.scrollable_frame, text="项目名称映射 (可选)", padding=10)
        project_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        # 说明文本
        ttk.Label(project_frame, 
                 text="格式: 项目名(分支名) -> 自定义名称\n例如: my-project(master) -> 我的项目-",
                 foreground="gray").pack(anchor="w", pady=(0, 5))
        
        # 文本编辑器
        self.project_names_text = scrolledtext.ScrolledText(
            project_frame, height=8, width=80, wrap=tk.WORD)
        self.project_names_text.pack(fill="both", expand=True)
    
    def create_action_section(self):
        """创建操作按钮区域"""
        action_frame = ttk.Frame(self.scrollable_frame, style='Custom.TFrame')
        action_frame.pack(fill="x", pady=10)
        
        # 按钮容器
        button_frame = ttk.Frame(action_frame)
        button_frame.pack(anchor="center")
        
        # 保存配置按钮
        save_btn = ttk.Button(button_frame, text="💾 保存配置", 
                             command=self.save_config, style='Custom.TButton')
        save_btn.pack(side="left", padx=5)
        
        # 加载配置按钮
        load_btn = ttk.Button(button_frame, text="📂 重新加载配置", 
                             command=self.load_config_to_gui, style='Custom.TButton')
        load_btn.pack(side="left", padx=5)
        
        # 开始提取按钮
        self.extract_btn = ttk.Button(button_frame, text="🚀 开始提取日志", 
                                     command=self.start_extraction, style='Custom.TButton')
        self.extract_btn.pack(side="left", padx=5)
        
        # 进度条
        self.progress = ttk.Progressbar(action_frame, mode='indeterminate')
        self.progress.pack(fill="x", pady=(10, 0))
    
    def create_log_section(self):
        """创建日志输出区域"""
        log_frame = ttk.LabelFrame(self.scrollable_frame, text="运行日志", padding=10)
        log_frame.pack(fill="both", expand=True, pady=(0, 10))
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame, height=10, width=80, wrap=tk.WORD,
            bg="#34495e", fg="white", insertbackground="white")
        self.log_text.pack(fill="both", expand=True)
        
        # 清空日志按钮
        clear_btn = ttk.Button(log_frame, text="清空日志", command=self.clear_log)
        clear_btn.pack(anchor="e", pady=(5, 0))
    
    def browse_root_directory(self):
        """浏览根目录"""
        directory = filedialog.askdirectory(title="选择Git仓库根目录")
        if directory:
            self.root_dir_var.set(directory)
    
    def browse_output_directory(self):
        """浏览输出目录"""
        directory = filedialog.askdirectory(title="选择输出目录")
        if directory:
            self.output_dir_var.set(directory)
    
    def log_message(self, message):
        """在日志区域添加消息"""
        self.log_text.insert(tk.END, f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def clear_log(self):
        """清空日志"""
        self.log_text.delete(1.0, tk.END)
    
    def parse_project_names(self):
        """解析项目名称映射文本"""
        project_names = {}
        text = self.project_names_text.get(1.0, tk.END).strip()
        
        for line in text.split('\n'):
            line = line.strip()
            if line and ' -> ' in line:
                try:
                    key, value = line.split(' -> ', 1)
                    project_names[key.strip()] = value.strip()
                except ValueError:
                    continue
        
        return project_names
    
    def format_project_names_text(self, project_names):
        """格式化项目名称映射为文本"""
        lines = []
        for key, value in project_names.items():
            lines.append(f"{key} -> {value}")
        return '\n'.join(lines)
    
    def save_config(self):
        """保存配置到YAML文件"""
        try:
            config = {
                'root_directory': self.root_dir_var.get(),
                'author': self.author_var.get(),
                'output_directory': self.output_dir_var.get(),
                'start_date': self.start_date_var.get(),
                'end_date': self.end_date_var.get(),
                'detailed_output': self.detailed_output_var.get(),
                'show_project_and_branch': self.show_project_branch_var.get(),
                'pull_latest_code': self.pull_latest_var.get(),
                'extract_all_branches': self.extract_all_branches_var.get(),
                'project_names': self.parse_project_names()
            }
            
            with open('config.yaml', 'w', encoding='utf-8') as f:
                yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
            
            self.log_message("✅ 配置已保存到 config.yaml")
            messagebox.showinfo("成功", "配置已成功保存!")
        
        except Exception as e:
            self.log_message(f"❌ 保存配置失败: {str(e)}")
            messagebox.showerror("错误", f"保存配置失败:\n{str(e)}")
    
    def load_config_to_gui(self):
        """从配置文件加载配置到GUI"""
        try:
            if os.path.exists('config.yaml'):
                config = load_config()
                
                self.root_dir_var.set(config.get('root_directory', ''))
                self.author_var.set(config.get('author', ''))
                self.output_dir_var.set(config.get('output_directory', ''))
                self.start_date_var.set(config.get('start_date', ''))
                self.end_date_var.set(config.get('end_date', ''))
                self.detailed_output_var.set(config.get('detailed_output', True))
                self.show_project_branch_var.set(config.get('show_project_and_branch', True))
                self.pull_latest_var.set(config.get('pull_latest_code', False))
                self.extract_all_branches_var.set(config.get('extract_all_branches', False))
                
                # 加载项目名称映射
                project_names = config.get('project_names', {})
                self.project_names_text.delete(1.0, tk.END)
                self.project_names_text.insert(1.0, self.format_project_names_text(project_names))
                
                self.log_message("✅ 配置已从 config.yaml 加载")
            else:
                self.log_message("⚠️ 配置文件不存在，使用默认值")
        
        except Exception as e:
            self.log_message(f"❌ 加载配置失败: {str(e)}")
            messagebox.showerror("错误", f"加载配置失败:\n{str(e)}")
    
    def validate_config(self):
        """验证配置"""
        if not self.root_dir_var.get():
            messagebox.showerror("错误", "请选择根目录!")
            return False
        
        if not self.author_var.get():
            messagebox.showerror("错误", "请输入作者名!")
            return False
        
        if not self.output_dir_var.get():
            messagebox.showerror("错误", "请选择输出目录!")
            return False
        
        if not os.path.exists(self.root_dir_var.get()):
            messagebox.showerror("错误", "根目录不存在!")
            return False
        
        if not os.path.exists(self.output_dir_var.get()):
            messagebox.showerror("错误", "输出目录不存在!")
            return False
        
        return True
    
    def start_extraction(self):
        """开始提取日志"""
        if not self.validate_config():
            return
        
        # 保存当前配置
        self.save_config()
        
        # 禁用按钮并开始进度条
        self.extract_btn.config(state='disabled')
        self.progress.start()
        
        # 在新线程中执行提取操作
        threading.Thread(target=self.extract_commits, daemon=True).start()
    
    def extract_commits(self):
        """提取提交记录的主要逻辑"""
        try:
            self.log_message("🔍 开始搜索Git仓库...")
            
            # 获取配置
            root_directory = self.root_dir_var.get()
            author = self.author_var.get()
            output_directory = self.output_dir_var.get()
            
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            start_date = self.start_date_var.get() or today
            end_date = self.end_date_var.get() or today
            
            detailed_output = self.detailed_output_var.get()
            project_names = self.parse_project_names()
            show_project_and_branch = self.show_project_branch_var.get()
            pull_latest_code = self.pull_latest_var.get()
            extract_all_branches = self.extract_all_branches_var.get()
            
            # 搜索Git仓库
            git_repos = find_git_repos(root_directory)
            self.log_message(f"✅ 找到 {len(git_repos)} 个Git仓库")
            
            all_commits = []
            all_messages = []
            
            # 处理每个仓库
            for i, repo in enumerate(git_repos, 1):
                self.log_message(f"📂 处理仓库 {i}/{len(git_repos)}: {os.path.basename(repo)}")
                
                commits, messages = get_git_commits(
                    repo, start_date, end_date, author, 
                    pull_latest_code, extract_all_branches
                )
                
                if commits:
                    all_commits.extend(commits)
                    all_messages.extend(messages)
                    self.log_message(f"   ✅ 找到 {len(commits)} 个提交")
                else:
                    self.log_message(f"   ⚪ 无提交记录")
            
            # 生成输出文件名
            if start_date == today and end_date == today:
                date_part = today
            else:
                date_part = f"{start_date}_to_{end_date}"
            
            output_file = os.path.join(output_directory, f"git_commits_{date_part}.txt")
            
            # 保存文件
            if all_commits:
                save_commits_to_file(
                    all_commits, all_messages, output_file,
                    detailed_output, project_names, show_project_and_branch
                )
                self.log_message(f"🎉 提取完成! 文件已保存至: {output_file}")
                self.log_message(f"📊 总共找到 {len(all_commits)} 个提交记录")
                
                # 询问是否打开文件
                self.root.after(0, lambda: self.ask_open_file(output_file))
            else:
                self.log_message(f"⚠️ 在 {start_date} 到 {end_date} 期间未找到任何提交记录")
                self.root.after(0, lambda: messagebox.showinfo("提示", "未找到任何提交记录"))
        
        except Exception as e:
            error_msg = f"❌ 提取过程中发生错误: {str(e)}"
            self.log_message(error_msg)
            self.root.after(0, lambda: messagebox.showerror("错误", error_msg))
        
        finally:
            # 恢复UI状态
            self.root.after(0, self.extraction_finished)
    
    def ask_open_file(self, file_path):
        """询问是否打开生成的文件"""
        result = messagebox.askyesno("提取完成", f"日志已成功提取!\n\n是否现在打开文件?\n{file_path}")
        if result:
            try:
                os.startfile(file_path)  # Windows
            except AttributeError:
                try:
                    os.system(f"open '{file_path}'")  # macOS
                except:
                    os.system(f"xdg-open '{file_path}'")  # Linux
    
    def extraction_finished(self):
        """提取完成后恢复UI状态"""
        self.progress.stop()
        self.extract_btn.config(state='normal')


def main():
    """主函数"""
    root = tk.Tk()
    app = GitCommitToolGUI(root)
    
    # 绑定鼠标滚轮
    def _on_mousewheel(event):
        app.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    app.canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    root.mainloop()


if __name__ == "__main__":
    main() 