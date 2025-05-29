@echo off
title Git提交日志提取工具 - 摸鱼神器 v1.0
chcp 65001 >nul

echo.
echo     ===================================================
echo     🚀 Git提交日志提取工具 - 摸鱼神器 v1.0
echo     ✨ 全新Material UI设计风格
echo     ===================================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误：未检测到Python环境
    echo 💡 请先安装Python 3.7+
    echo 📥 下载地址：https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo ✅ Python环境检测通过

REM 检查依赖是否安装
echo 📦 检查依赖包...
python -c "import yaml, tkcalendar" >nul 2>&1
if errorlevel 1 (
    echo 📦 正在安装必要的依赖包...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ 依赖安装失败，请检查网络连接或尝试手动安装
        echo 💡 手动安装命令：pip install pyyaml tkcalendar pillow
        pause
        exit /b 1
    )
    echo ✅ 依赖安装完成
) else (
    echo ✅ 依赖包检查通过
)

echo 🔍 检查核心文件...
if not exist "gui.py" (
    echo ❌ 未找到 gui.py 文件
    echo 💡 请确保在正确的目录中运行此脚本
    pause
    exit /b 1
)

if not exist "git_commit_tool.py" (
    echo ❌ 未找到 git_commit_tool.py 文件
    echo 💡 请确保所有核心文件都存在
    pause
    exit /b 1
)

echo ✅ 核心文件检查通过

echo.
echo 🚀 正在启动全新的Material UI界面...
echo 🎨 享受现代化的用户体验！
echo.

REM 启动GUI应用
python gui.py

if errorlevel 1 (
    echo.
    echo ❌ 程序运行出错
    echo 💡 请检查错误信息并重试
    echo 🔧 如果问题持续存在，请尝试重新安装依赖
    echo.
    pause
)

echo.
echo 👋 程序已退出，感谢使用Material UI风格的摸鱼神器！
pause 