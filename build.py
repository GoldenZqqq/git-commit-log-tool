#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Git提交日志提取工具 - 打包脚本
使用PyInstaller将GUI应用打包为exe文件
"""

import os
import sys
import shutil
import subprocess

def install_dependencies():
    """安装必要的依赖"""
    print("📦 正在安装依赖...")
    
    dependencies = [
        'pyinstaller',
        'pyyaml',
        'pillow',  # 如果需要图标支持
    ]
    
    for dep in dependencies:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', dep])
            print(f"✅ 已安装 {dep}")
        except subprocess.CalledProcessError as e:
            print(f"❌ 安装 {dep} 失败: {e}")
            return False
    
    return True

def create_spec_file():
    """创建PyInstaller规格文件"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['gui.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('config.yaml', '.'),
        ('README.md', '.'),
        ('LICENSE', '.'),
    ],
    hiddenimports=[
        'yaml',
        'tkinter',
        'tkinter.ttk',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'tkinter.scrolledtext',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='GitCommitTool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # 设置为False以隐藏控制台窗口
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
    version='version_info.txt' if os.path.exists('version_info.txt') else None,
)
'''
    
    with open('GitCommitTool.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("✅ 已创建 GitCommitTool.spec 文件")

def create_version_info():
    """创建版本信息文件"""
    version_info = '''# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1,0,0,0),
    prodvers=(1,0,0,0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Git提交日志提取工具'),
         StringStruct(u'FileDescription', u'Git提交日志提取工具 - 摸鱼神器'),
         StringStruct(u'FileVersion', u'1.0.0.0'),
         StringStruct(u'InternalName', u'GitCommitTool'),
         StringStruct(u'LegalCopyright', u'Copyright © 2024'),
         StringStruct(u'OriginalFilename', u'GitCommitTool.exe'),
         StringStruct(u'ProductName', u'Git提交日志提取工具'),
         StringStruct(u'ProductVersion', u'1.0.0.0')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
'''
    
    with open('version_info.txt', 'w', encoding='utf-8') as f:
        f.write(version_info)
    
    print("✅ 已创建 version_info.txt 文件")

def create_icon():
    """创建应用图标（如果不存在）"""
    if not os.path.exists('icon.ico'):
        print("⚠️ 未找到 icon.ico 文件，将跳过图标设置")
        print("💡 提示：你可以添加一个 icon.ico 文件来自定义应用图标")

def build_exe():
    """构建exe文件"""
    print("🔨 开始构建exe文件...")
    
    try:
        # 使用规格文件构建
        cmd = [sys.executable, '-m', 'PyInstaller', '--clean', 'GitCommitTool.spec']
        subprocess.check_call(cmd)
        print("✅ 构建完成!")
        
        # 检查输出文件
        dist_path = os.path.join('dist', 'GitCommitTool.exe')
        if os.path.exists(dist_path):
            file_size = os.path.getsize(dist_path) / (1024 * 1024)  # MB
            print(f"📁 输出文件: {dist_path}")
            print(f"📊 文件大小: {file_size:.2f} MB")
            return True
        else:
            print("❌ 未找到构建的exe文件")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ 构建失败: {e}")
        return False

def create_portable_package():
    """创建便携版包"""
    print("📦 正在创建便携版包...")
    
    package_dir = "GitCommitTool_Portable"
    if os.path.exists(package_dir):
        shutil.rmtree(package_dir)
    
    os.makedirs(package_dir)
    
    # 复制exe文件
    exe_src = os.path.join('dist', 'GitCommitTool.exe')
    if os.path.exists(exe_src):
        shutil.copy2(exe_src, package_dir)
    
    # 复制配置文件
    files_to_copy = ['config.yaml', 'README.md', 'LICENSE']
    for file_name in files_to_copy:
        if os.path.exists(file_name):
            shutil.copy2(file_name, package_dir)
    
    # 创建启动说明
    readme_content = """# Git提交日志提取工具 - 便携版

## 使用说明

1. 双击 `GitCommitTool.exe` 启动程序
2. 配置相关参数后点击"开始提取日志"即可使用
3. 所有配置会自动保存到 `config.yaml` 文件中

## 文件说明

- `GitCommitTool.exe` - 主程序
- `config.yaml` - 配置文件
- `README.md` - 项目说明文档
- `LICENSE` - 许可证文件

如有问题，请查看项目主页获取帮助。
"""
    
    with open(os.path.join(package_dir, "使用说明.txt"), 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✅ 便携版包已创建: {package_dir}/")

def cleanup():
    """清理构建文件"""
    cleanup_dirs = ['build', '__pycache__']
    cleanup_files = ['GitCommitTool.spec', 'version_info.txt']
    
    print("🧹 正在清理构建文件...")
    
    for dir_name in cleanup_dirs:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"✅ 已删除 {dir_name}/")
    
    for file_name in cleanup_files:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"✅ 已删除 {file_name}")

def main():
    """主函数"""
    print("🚀 Git提交日志提取工具 - 自动打包脚本")
    print("=" * 50)
    
    # 检查必要文件
    required_files = ['gui.py', 'git_commit_tool.py', 'main.py']
    for file_name in required_files:
        if not os.path.exists(file_name):
            print(f"❌ 缺少必要文件: {file_name}")
            return
    
    try:
        # 1. 安装依赖
        if not install_dependencies():
            print("❌ 依赖安装失败，退出构建")
            return
        
        # 2. 创建必要的构建文件
        create_spec_file()
        create_version_info()
        create_icon()
        
        # 3. 构建exe
        if not build_exe():
            print("❌ 构建失败")
            return
        
        # 4. 创建便携版包
        create_portable_package()
        
        # 5. 清理（可选）
        response = input("\n🗑️ 是否清理构建文件? (y/n): ").lower()
        if response == 'y':
            cleanup()
        
        print("\n🎉 打包完成!")
        print("📁 可执行文件位置: dist/GitCommitTool.exe")
        print("📦 便携版位置: GitCommitTool_Portable/")
        
    except KeyboardInterrupt:
        print("\n⚠️ 构建被用户中断")
    except Exception as e:
        print(f"❌ 构建过程中发生错误: {e}")

if __name__ == "__main__":
    main() 