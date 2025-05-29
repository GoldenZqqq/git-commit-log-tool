import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import datetime
import json
import threading
from git_commit_tool import find_git_repos, get_git_commits, save_commits_to_file, load_config
import yaml
from tkcalendar import DateEntry

class GitCommitToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Git 提交日志提取工具")
        self.root.geometry("750x650")  # 减小宽度从900到750
        self.root.resizable(True, True)
        
        # Material UI 配色方案
        self.colors = {
            'primary': '#1976D2',        # Material Blue 700
            'primary_light': '#42A5F5',  # Material Blue 400
            'primary_dark': '#1565C0',   # Material Blue 800
            'secondary': '#FF9800',      # Material Orange 500
            'background': '#FAFAFA',     # Material Grey 50
            'surface': '#FFFFFF',        # White
            'surface_variant': '#F5F5F5', # Material Grey 100
            'on_primary': '#FFFFFF',     # White
            'on_surface': '#212121',     # Material Grey 900
            'on_surface_variant': '#757575', # Material Grey 600
            'success': '#4CAF50',        # Material Green 500
            'warning': '#FF9800',        # Material Orange 500
            'error': '#F44336',          # Material Red 500
            'border': '#E0E0E0',         # Material Grey 300
            'shadow': '#00000020'        # Light shadow
        }
        
        self.root.configure(bg=self.colors['background'])
        
        # 创建样式
        self.setup_styles()
        
        # 创建主框架
        self.create_main_frame()
        
        # 加载配置
        self.load_config_to_gui()
    
    def setup_styles(self):
        """设置Material UI样式"""
        style = ttk.Style()
        
        # 使用更现代的主题
        try:
            style.theme_use('vista')  # Windows 现代主题
        except:
            try:
                style.theme_use('clam')  # 备选主题
            except:
                style.theme_use('default')
        
        # 配置标题样式
        style.configure('Title.TLabel', 
                       background=self.colors['background'],
                       foreground=self.colors['primary'], 
                       font=('Segoe UI', 20, 'bold'))
        
        # 配置子标题样式
        style.configure('Heading.TLabel', 
                       background=self.colors['background'],
                       foreground=self.colors['on_surface'], 
                       font=('Segoe UI', 12, 'bold'))
        
        # 配置普通标签样式
        style.configure('Normal.TLabel', 
                       background=self.colors['background'],
                       foreground=self.colors['on_surface_variant'], 
                       font=('Segoe UI', 9))
        
        # 配置框架样式
        style.configure('Card.TFrame', 
                       background=self.colors['surface'],
                       relief='flat',
                       borderwidth=1)
        
        style.configure('Main.TFrame', 
                       background=self.colors['background'])
        
        # 配置按钮样式 - 修复颜色问题
        style.configure('Primary.TButton', 
                       background=self.colors['primary'],
                       foreground='white',  # 强制设置为白色
                       font=('Segoe UI', 10, 'bold'),
                       focuscolor='none',
                       borderwidth=0,
                       relief='flat',
                       padding=(20, 8))  # 增加内边距
        
        style.map('Primary.TButton',
                 background=[('active', self.colors['primary_light']),
                           ('pressed', self.colors['primary_dark']),
                           ('disabled', '#CCCCCC')],
                 foreground=[('active', 'white'),
                           ('pressed', 'white'),
                           ('disabled', '#666666')])
        
        style.configure('Secondary.TButton', 
                       background=self.colors['surface_variant'],
                       foreground=self.colors['on_surface'],
                       font=('Segoe UI', 9),
                       focuscolor='none',
                       borderwidth=1,
                       relief='flat',
                       padding=(10, 6))
        
        style.map('Secondary.TButton',
                 background=[('active', self.colors['border']),
                           ('pressed', self.colors['surface_variant'])],
                 foreground=[('active', self.colors['on_surface']),
                           ('pressed', self.colors['on_surface'])])
        
        # 配置输入框样式
        style.configure('Modern.TEntry',
                       fieldbackground=self.colors['surface'],
                       borderwidth=1,
                       relief='solid',
                       bordercolor=self.colors['border'],
                       font=('Segoe UI', 9))
        
        style.map('Modern.TEntry',
                 bordercolor=[('focus', self.colors['primary'])])
        
        # 配置LabelFrame样式
        style.configure('Card.TLabelframe',
                       background=self.colors['surface'],
                       borderwidth=0,
                       relief='flat')
        
        style.configure('Card.TLabelframe.Label',
                       background=self.colors['surface'],
                       foreground=self.colors['primary'],
                       font=('Segoe UI', 11, 'bold'))
        
        # 配置复选框样式
        style.configure('Modern.TCheckbutton',
                       background=self.colors['surface'],
                       foreground=self.colors['on_surface'],
                       font=('Segoe UI', 9),
                       focuscolor='none')
        
        # 配置进度条样式
        style.configure('Modern.Horizontal.TProgressbar',
                       background=self.colors['primary'],
                       troughcolor=self.colors['surface_variant'],
                       borderwidth=0,
                       lightcolor=self.colors['primary'],
                       darkcolor=self.colors['primary'])
    
    def create_main_frame(self):
        """创建主界面框架"""
        # 创建主容器
        main_container = tk.Frame(self.root, bg=self.colors['background'])
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # 创建滚动框架
        self.canvas = tk.Canvas(main_container, 
                               bg=self.colors['background'], 
                               highlightthickness=0,
                               bd=0)
        
        # 自定义滚动条
        scrollbar_frame = tk.Frame(main_container, bg=self.colors['background'])
        self.scrollbar = ttk.Scrollbar(scrollbar_frame, orient="vertical", command=self.canvas.yview)
        
        self.scrollable_frame = ttk.Frame(self.canvas, style='Main.TFrame')
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # 布局滚动组件
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar_frame.pack(side="right", fill="y", padx=(10, 0))
        self.scrollbar.pack(fill="y")
        
        # 主标题
        title_frame = ttk.Frame(self.scrollable_frame, style='Main.TFrame')
        title_frame.pack(fill="x", pady=(0, 30))
        
        title_label = ttk.Label(title_frame, 
                              text="🚀 Git 提交日志提取工具", 
                              style='Title.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(title_frame, 
                                 text="现代化的代码提交记录管理工具", 
                                 style='Normal.TLabel')
        subtitle_label.pack(pady=(5, 0))
        
        # 创建各个区域
        self.create_config_section()
        self.create_advanced_section()
        self.create_project_names_section()
        self.create_action_section()
        self.create_log_section()
    
    def create_card_frame(self, parent, title, pady=(0, 20)):
        """创建卡片式框架"""
        card_frame = ttk.LabelFrame(parent, text=title, style='Card.TLabelframe', padding=20)
        card_frame.pack(fill="x", pady=pady)
        return card_frame
    
    def create_config_section(self):
        """创建基本配置区域"""
        config_frame = self.create_card_frame(self.scrollable_frame, "📋 基本配置")
        
        # 根目录选择
        self.create_file_input(config_frame, "根目录:", 0, is_directory=True, browse_func=self.browse_root_directory)
        
        # 作者名
        self.create_text_input(config_frame, "作者名:", 1)
        
        # 输出目录选择  
        self.create_file_input(config_frame, "输出目录:", 2, is_directory=True, browse_func=self.browse_output_directory)
        
        # 日期选择器
        self.create_date_inputs(config_frame, 3)
        
        # 配置grid权重
        config_frame.columnconfigure(1, weight=1)
    
    def create_text_input(self, parent, label_text, row):
        """创建文本输入控件"""
        ttk.Label(parent, text=label_text, style='Normal.TLabel').grid(
            row=row, column=0, sticky="w", pady=(0, 15), padx=(0, 15))
        
        if label_text == "作者名:":
            self.author_var = tk.StringVar()
            entry = ttk.Entry(parent, textvariable=self.author_var, 
                            style='Modern.TEntry', font=('Segoe UI', 10), width=30)
        
        entry.grid(row=row, column=1, sticky="ew", pady=(0, 15))
        return entry
    
    def create_file_input(self, parent, label_text, row, is_directory=True, browse_func=None):
        """创建文件/目录选择控件"""
        ttk.Label(parent, text=label_text, style='Normal.TLabel').grid(
            row=row, column=0, sticky="w", pady=(0, 15), padx=(0, 15))
        
        # 创建输入框架
        input_frame = ttk.Frame(parent, style='Main.TFrame')
        input_frame.grid(row=row, column=1, sticky="ew", pady=(0, 15), columnspan=2)
        input_frame.columnconfigure(0, weight=1)
        
        # 根据标签设置变量
        if "根目录" in label_text:
            self.root_dir_var = tk.StringVar()
            var = self.root_dir_var
        elif "输出目录" in label_text:
            self.output_dir_var = tk.StringVar()
            var = self.output_dir_var
        
        entry = ttk.Entry(input_frame, textvariable=var, 
                        style='Modern.TEntry', font=('Segoe UI', 10))
        entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        
        browse_btn = ttk.Button(input_frame, text="📁 浏览", 
                              command=browse_func, style='Secondary.TButton')
        browse_btn.grid(row=0, column=1)
        
        return entry
    
    def create_date_inputs(self, parent, start_row):
        """创建日期选择控件"""
        # 开始日期
        ttk.Label(parent, text="开始日期:", style='Normal.TLabel').grid(
            row=start_row, column=0, sticky="w", pady=(0, 15), padx=(0, 15))
        
        date_frame1 = ttk.Frame(parent, style='Main.TFrame')
        date_frame1.grid(row=start_row, column=1, sticky="ew", pady=(0, 15))
        
        self.start_date_entry = DateEntry(date_frame1,
                                        width=12,
                                        background=self.colors['primary'],
                                        foreground=self.colors['on_primary'],
                                        borderwidth=0,
                                        font=('Segoe UI', 10),
                                        date_pattern='yyyy-mm-dd',
                                        state='readonly')
        self.start_date_entry.pack(side="left")
        
        # 清空按钮
        clear_btn1 = ttk.Button(date_frame1, text="清空", 
                              command=self.clear_start_date, style='Secondary.TButton')
        clear_btn1.pack(side="left", padx=(10, 0))
        
        ttk.Label(parent, text="(可选，留空默认为今天)", 
                 style='Normal.TLabel', foreground=self.colors['on_surface_variant']).grid(
            row=start_row, column=2, sticky="w", pady=(0, 15), padx=(10, 0))
        
        # 结束日期
        ttk.Label(parent, text="结束日期:", style='Normal.TLabel').grid(
            row=start_row+1, column=0, sticky="w", pady=(0, 15), padx=(0, 15))
        
        date_frame2 = ttk.Frame(parent, style='Main.TFrame')
        date_frame2.grid(row=start_row+1, column=1, sticky="ew", pady=(0, 15))
        
        self.end_date_entry = DateEntry(date_frame2,
                                      width=12,
                                      background=self.colors['primary'],
                                      foreground=self.colors['on_primary'],
                                      borderwidth=0,
                                      font=('Segoe UI', 10),
                                      date_pattern='yyyy-mm-dd',
                                      state='readonly')
        self.end_date_entry.pack(side="left")
        
        # 清空按钮
        clear_btn2 = ttk.Button(date_frame2, text="清空", 
                              command=self.clear_end_date, style='Secondary.TButton')
        clear_btn2.pack(side="left", padx=(10, 0))
        
        ttk.Label(parent, text="(可选，留空默认为今天)", 
                 style='Normal.TLabel', foreground=self.colors['on_surface_variant']).grid(
            row=start_row+1, column=2, sticky="w", pady=(0, 15), padx=(10, 0))
        
        # 快捷日期按钮
        quick_date_frame = ttk.Frame(parent, style='Main.TFrame')
        quick_date_frame.grid(row=start_row+2, column=1, sticky="ew", pady=(0, 15), columnspan=2)
        
        ttk.Label(quick_date_frame, text="快捷选择:", style='Normal.TLabel').pack(side="left")
        
        ttk.Button(quick_date_frame, text="今天", 
                  command=self.set_today, style='Secondary.TButton').pack(side="left", padx=(10, 5))
        ttk.Button(quick_date_frame, text="最近7天", 
                  command=self.set_last_week, style='Secondary.TButton').pack(side="left", padx=5)
        ttk.Button(quick_date_frame, text="本月", 
                  command=self.set_this_month, style='Secondary.TButton').pack(side="left", padx=5)
    
    def clear_start_date(self):
        """清空开始日期"""
        self.start_date_entry.set_date(datetime.date.today())
        
    def clear_end_date(self):
        """清空结束日期"""
        self.end_date_entry.set_date(datetime.date.today())
        
    def set_today(self):
        """设置为今天"""
        today = datetime.date.today()
        self.start_date_entry.set_date(today)
        self.end_date_entry.set_date(today)
        
    def set_last_week(self):
        """设置为最近7天"""
        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=7)
        self.start_date_entry.set_date(week_ago)
        self.end_date_entry.set_date(today)
        
    def set_this_month(self):
        """设置为本月"""
        today = datetime.date.today()
        month_start = today.replace(day=1)
        self.start_date_entry.set_date(month_start)
        self.end_date_entry.set_date(today)
    
    def create_advanced_section(self):
        """创建高级选项区域"""
        advanced_frame = self.create_card_frame(self.scrollable_frame, "⚙️ 高级选项")
        
        # 创建两列布局
        left_frame = ttk.Frame(advanced_frame, style='Main.TFrame')
        right_frame = ttk.Frame(advanced_frame, style='Main.TFrame')
        
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 20))
        right_frame.pack(side="left", fill="both", expand=True)
        
        # 左列选项
        self.detailed_output_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(left_frame, text="📄 输出详细日志", 
                       variable=self.detailed_output_var, style='Modern.TCheckbutton').pack(anchor="w", pady=5)
        
        self.pull_latest_var = tk.BooleanVar()
        ttk.Checkbutton(left_frame, text="🔄 提取前拉取最新代码", 
                       variable=self.pull_latest_var, style='Modern.TCheckbutton').pack(anchor="w", pady=5)
        
        # 右列选项
        self.show_project_branch_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(right_frame, text="🏷️ 显示项目名与分支名", 
                       variable=self.show_project_branch_var, style='Modern.TCheckbutton').pack(anchor="w", pady=5)
        
        self.extract_all_branches_var = tk.BooleanVar()
        ttk.Checkbutton(right_frame, text="🌿 提取所有分支的提交记录", 
                       variable=self.extract_all_branches_var, style='Modern.TCheckbutton').pack(anchor="w", pady=5)
    
    def create_project_names_section(self):
        """创建项目名称映射区域"""
        project_frame = self.create_card_frame(self.scrollable_frame, "🎯 项目名称映射 (可选)")
        
        # 说明文本
        help_frame = ttk.Frame(project_frame, style='Main.TFrame')
        help_frame.pack(fill="x", pady=(0, 15))
        
        help_label = ttk.Label(help_frame, 
                             text="💡 格式说明：项目名(分支名) -> 自定义名称",
                             style='Normal.TLabel',
                             foreground=self.colors['on_surface_variant'])
        help_label.pack(anchor="w")
        
        example_label = ttk.Label(help_frame, 
                                text="   示例：my-project(master) -> 我的项目-",
                                style='Normal.TLabel',
                                foreground=self.colors['on_surface_variant'])
        example_label.pack(anchor="w")
        
        # 文本编辑器容器
        text_container = tk.Frame(project_frame, bg=self.colors['surface'], relief='solid', bd=1)
        text_container.pack(fill="both", expand=True)
        
        self.project_names_text = scrolledtext.ScrolledText(
            text_container, 
            height=8, 
            wrap=tk.WORD,
            bg=self.colors['surface'],
            fg=self.colors['on_surface'],
            font=('Consolas', 10),
            insertbackground=self.colors['primary'],
            selectbackground=self.colors['primary_light'],
            selectforeground=self.colors['on_primary'],
            relief='flat',
            bd=0)
        self.project_names_text.pack(fill="both", expand=True, padx=8, pady=8)
    
    def create_action_section(self):
        """创建操作按钮区域"""
        action_frame = ttk.Frame(self.scrollable_frame, style='Main.TFrame')
        action_frame.pack(fill="x", pady=(20, 0))
        
        # 按钮容器
        button_frame = ttk.Frame(action_frame, style='Main.TFrame')
        button_frame.pack(anchor="center")
        
        # 保存配置按钮
        save_btn = ttk.Button(button_frame, text="💾 保存配置", 
                             command=self.save_config, style='Secondary.TButton')
        save_btn.pack(side="left", padx=(0, 10))
        
        # 加载配置按钮
        load_btn = ttk.Button(button_frame, text="📂 重新加载配置", 
                             command=self.load_config_to_gui, style='Secondary.TButton')
        load_btn.pack(side="left", padx=(0, 10))
        
        # 主要操作按钮 - 使用tk.Button确保颜色正确显示
        self.extract_btn = tk.Button(button_frame, 
                                   text="🚀 开始提取日志",
                                   command=self.start_extraction,
                                   bg=self.colors['primary'],
                                   fg='white',
                                   font=('Segoe UI', 10, 'bold'),
                                   relief='flat',
                                   borderwidth=0,
                                   padx=20,
                                   pady=8,
                                   cursor='hand2',
                                   activebackground=self.colors['primary_light'],
                                   activeforeground='white')
        self.extract_btn.pack(side="left", padx=(10, 0))
        
        # 进度条
        progress_frame = ttk.Frame(action_frame, style='Main.TFrame')
        progress_frame.pack(fill="x", pady=(15, 0))
        
        self.progress = ttk.Progressbar(progress_frame, mode='indeterminate', 
                                      style='Modern.Horizontal.TProgressbar')
        self.progress.pack(fill="x")
    
    def create_log_section(self):
        """创建日志输出区域"""
        log_frame = self.create_card_frame(self.scrollable_frame, "📋 运行日志", pady=(20, 0))
        
        # 日志容器
        log_container = tk.Frame(log_frame, bg=self.colors['on_surface'], relief='solid', bd=1)
        log_container.pack(fill="both", expand=True)
        
        self.log_text = scrolledtext.ScrolledText(
            log_container, 
            height=12, 
            wrap=tk.WORD,
            bg=self.colors['on_surface'],
            fg=self.colors['surface'],
            font=('Consolas', 9),
            insertbackground=self.colors['surface'],
            selectbackground=self.colors['primary'],
            selectforeground=self.colors['on_primary'],
            relief='flat',
            bd=0)
        self.log_text.pack(fill="both", expand=True, padx=8, pady=8)
        
        # 清空日志按钮
        clear_btn = ttk.Button(log_frame, text="🗑️ 清空日志", 
                              command=self.clear_log, style='Secondary.TButton')
        clear_btn.pack(anchor="e", pady=(10, 0))
    
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
        timestamp = datetime.datetime.now().strftime('%H:%M:%S')
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def clear_log(self):
        """清空日志"""
        self.log_text.delete(1.0, tk.END)
        self.log_message("📝 日志已清空")
    
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
    
    def get_date_string(self, date_entry, clear_if_today=True):
        """获取日期字符串，如果是今天且clear_if_today为True则返回空字符串"""
        selected_date = date_entry.get_date()
        today = datetime.date.today()
        
        if clear_if_today and selected_date == today:
            return ""
        return selected_date.strftime('%Y-%m-%d')
    
    def save_config(self):
        """保存配置到YAML文件"""
        try:
            config = {
                'root_directory': self.root_dir_var.get(),
                'author': self.author_var.get(),
                'output_directory': self.output_dir_var.get(),
                'start_date': self.get_date_string(self.start_date_entry),
                'end_date': self.get_date_string(self.end_date_entry),
                'detailed_output': self.detailed_output_var.get(),
                'show_project_and_branch': self.show_project_branch_var.get(),
                'pull_latest_code': self.pull_latest_var.get(),
                'extract_all_branches': self.extract_all_branches_var.get(),
                'project_names': self.parse_project_names()
            }
            
            with open('config.yaml', 'w', encoding='utf-8') as f:
                yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
            
            self.log_message("✅ 配置已保存到 config.yaml")
            messagebox.showinfo("保存成功", "配置已成功保存到 config.yaml 文件！", icon='info')
        
        except Exception as e:
            self.log_message(f"❌ 保存配置失败: {str(e)}")
            messagebox.showerror("保存失败", f"保存配置时发生错误：\n{str(e)}")
    
    def load_config_to_gui(self):
        """从配置文件加载配置到GUI"""
        try:
            if os.path.exists('config.yaml'):
                config = load_config()
                
                self.root_dir_var.set(config.get('root_directory', ''))
                self.author_var.set(config.get('author', ''))
                self.output_dir_var.set(config.get('output_directory', ''))
                
                # 处理日期设置
                start_date = config.get('start_date', '')
                end_date = config.get('end_date', '')
                
                if start_date:
                    try:
                        date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
                        self.start_date_entry.set_date(date_obj)
                    except:
                        self.start_date_entry.set_date(datetime.date.today())
                else:
                    self.start_date_entry.set_date(datetime.date.today())
                
                if end_date:
                    try:
                        date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
                        self.end_date_entry.set_date(date_obj)
                    except:
                        self.end_date_entry.set_date(datetime.date.today())
                else:
                    self.end_date_entry.set_date(datetime.date.today())
                
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
            messagebox.showerror("加载失败", f"加载配置时发生错误：\n{str(e)}")
    
    def validate_config(self):
        """验证配置"""
        if not self.root_dir_var.get():
            messagebox.showerror("配置错误", "请选择根目录！", icon='error')
            return False
        
        if not self.author_var.get():
            messagebox.showerror("配置错误", "请输入作者名！", icon='error')
            return False
        
        if not self.output_dir_var.get():
            messagebox.showerror("配置错误", "请选择输出目录！", icon='error')
            return False
        
        if not os.path.exists(self.root_dir_var.get()):
            messagebox.showerror("配置错误", "根目录不存在！", icon='error')
            return False
        
        if not os.path.exists(self.output_dir_var.get()):
            messagebox.showerror("配置错误", "输出目录不存在！", icon='error')
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
            
            # 获取日期
            start_date = self.get_date_string(self.start_date_entry, clear_if_today=False)
            end_date = self.get_date_string(self.end_date_entry, clear_if_today=False)
            
            # 如果日期和今天相同，使用今天的字符串以符合原有逻辑
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            if not start_date or start_date == today:
                start_date = today
            if not end_date or end_date == today:
                end_date = today
            
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
                self.root.after(0, lambda: messagebox.showinfo("提示", "未找到任何提交记录", icon='info'))
        
        except Exception as e:
            error_msg = f"❌ 提取过程中发生错误: {str(e)}"
            self.log_message(error_msg)
            self.root.after(0, lambda: messagebox.showerror("错误", error_msg))
        
        finally:
            # 恢复UI状态
            self.root.after(0, self.extraction_finished)
    
    def ask_open_file(self, file_path):
        """询问是否打开生成的文件"""
        result = messagebox.askyesno("提取完成", 
                                   f"日志已成功提取!\n\n文件位置：{file_path}\n\n是否现在打开文件？", 
                                   icon='question')
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
        self.log_message("🏁 操作完成")


def main():
    """主函数"""
    root = tk.Tk()
    
    # 设置窗口图标（如果有的话）
    try:
        root.iconbitmap('icon.ico')
    except:
        pass
    
    app = GitCommitToolGUI(root)
    
    # 绑定鼠标滚轮
    def _on_mousewheel(event):
        app.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    app.canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    # 优雅退出
    def on_closing():
        root.quit()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == "__main__":
    main() 