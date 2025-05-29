@echo off
title Git提交日志提取工具 - 摸鱼神器
chcp 65001 >nul

echo.
echo     ===================================================
echo     🚀 Git提交日志提取工具 - 摸鱼神器
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
python -c "import yaml" >nul 2>&1
if errorlevel 1 (
    echo 📦 正在安装依赖包...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ 依赖安装失败
        pause
        exit /b 1
    )
    echo ✅ 依赖安装完成
)

echo 🔍 检查核心文件...
if not exist "gui.py" (
    echo ❌ 未找到 gui.py 文件
    pause
    exit /b 1
)

if not exist "git_commit_tool.py" (
    echo ❌ 未找到 git_commit_tool.py 文件
    pause
    exit /b 1
)

echo ✅ 核心文件检查通过

echo.
echo 🚀 正在启动GUI界面...
echo.

REM 启动GUI应用
python gui.py

if errorlevel 1 (
    echo.
    echo ❌ 程序运行出错
    echo 💡 请检查错误信息并重试
    echo.
    pause
)

echo.
echo 👋 程序已退出，感谢使用！
pause 