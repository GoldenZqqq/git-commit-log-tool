# 📦 GitHub Release 发布指南

## 🚀 发布准备

### 1. 版本准备
确保所有文件版本号已更新为 v1.0：
- [x] `start.bat` - 标题和描述
- [x] `build.py` - 版本信息文件
- [x] `gui.py` - 窗口标题
- [x] `README.md` - 项目说明

### 2. 构建可执行文件
```bash
# 运行打包脚本
python build.py

# 检查生成的文件
ls dist/
ls GitCommitTool_Portable/
```

### 3. 测试验证
- [ ] 测试GUI界面正常启动
- [ ] 测试所有功能正常工作
- [ ] 测试exe文件独立运行
- [ ] 验证配置文件读写正常

## 📋 GitHub Release 步骤

### Step 1: 推送代码到GitHub
```bash
# 添加所有更改
git add .

# 提交更改
git commit -m "🎉 v1.0 Release: Material UI重构完成

✨ 主要特性:
- Material UI风格界面重构
- 可视化日期选择器
- 现代化卡片布局
- 优化的用户体验
- 完整的打包系统

🔧 技术改进:
- 新增tkcalendar依赖
- 响应式界面设计
- 统一的颜色主题系统
- 增强的错误处理

📦 发布内容:
- 源代码
- Windows可执行文件
- 便携版包
- 完整文档"

# 推送到远程仓库
git push origin main
```

### Step 2: 创建Git标签
```bash
# 创建v1.0标签
git tag -a v1.0 -m "🎉 v1.0 正式版发布

🌟 重大更新:
- 全新Material UI界面设计
- 可视化日期选择功能
- 现代化的用户体验
- 完善的打包和文档系统

这是第一个正式版本，标志着项目从概念验证到成熟产品的转变。"

# 推送标签到远程
git push origin v1.0
```

### Step 3: 在GitHub网站创建Release

1. **访问GitHub仓库页面**
   - 打开你的仓库主页
   - 点击右侧的 "Releases" 链接

2. **创建新Release**
   - 点击 "Create a new release" 按钮
   - 或点击 "Draft a new release"

3. **填写Release信息**

   **Tag version:** `v1.0`
   
   **Release title:** `🎉 v1.0 - Material UI重构正式版`
   
   **Release notes:**
   ```markdown
   ## 🎉 Git提交日志提取工具 v1.0 正式发布！
   
   这是第一个正式版本，经过完全重构的Material UI风格界面，为用户带来全新的使用体验！
   
   ### 🌟 主要特性
   - **🎨 Material UI设计** - 采用Google Material Design规范，界面清新现代
   - **🗓️ 可视化日期选择** - 告别手动输入，点击即可选择日期
   - **⚡ 快捷操作** - 一键设置"今天"、"最近7天"、"本月"
   - **🃏 卡片布局** - 功能模块清晰分离，操作更直观
   - **📱 响应式设计** - 适配不同屏幕尺寸
   
   ### 🔧 技术改进
   - 全新的颜色系统和主题管理
   - 优化的界面布局和交互体验
   - 增强的错误处理和用户提示
   - 完善的打包和部署系统
   
   ### 📦 下载说明
   - **源码包** - 适合开发者，需要Python环境
   - **Windows可执行文件** - 开箱即用，无需安装Python
   - **便携版** - 包含所有文件的完整包
   
   ### 🚀 快速开始
   1. 下载对应的文件包
   2. Windows用户可直接运行 `GitCommitTool.exe`
   3. 源码用户运行 `start.bat` 或 `python gui.py`
   4. 配置Git仓库路径和作者信息
   5. 享受摸鱼的快乐时光！
   
   ### 📚 文档资源
   - [使用指南](./USAGE.md)
   - [Material UI升级说明](./MATERIAL_UI_UPGRADE.md)
   - [贡献指南](./CONTRIBUTING.md)
   
   ---
   
   **🙏 感谢支持！如果觉得有用，请给个⭐️**
   ```

4. **上传文件**
   - 将以下文件拖拽到Release页面的文件上传区域：
     - `dist/GitCommitTool.exe` (重命名为 `GitCommitTool-v1.0-Windows.exe`)
     - 压缩后的 `GitCommitTool_Portable` 文件夹 (命名为 `GitCommitTool-v1.0-Portable.zip`)
     - 可选：项目源码压缩包

### Step 4: 发布设置

1. **Pre-release设置**
   - 如果这是beta版本，勾选 "This is a pre-release"
   - 正式版本不需要勾选

2. **Release类型**
   - 勾选 "Set as the latest release" (设为最新版本)

3. **发布**
   - 点击 "Publish release" 按钮完成发布

## 📋 发布后的工作

### 1. 更新README
确保README中的下载链接指向新的Release：
```markdown
### 📥 下载

- [最新版本 v1.0](https://github.com/yourusername/git-commit-log-tool/releases/latest)
- [Windows可执行文件](https://github.com/yourusername/git-commit-log-tool/releases/download/v1.0/GitCommitTool-v1.0-Windows.exe)
- [便携版](https://github.com/yourusername/git-commit-log-tool/releases/download/v1.0/GitCommitTool-v1.0-Portable.zip)
```

### 2. 社交媒体推广
- 在技术社区分享你的项目
- 写博客介绍项目特性
- 在相关的GitHub话题中推广

### 3. 收集反馈
- 关注GitHub Issues
- 回复用户问题和建议
- 根据反馈规划下一版本

## 🔄 自动化发布 (高级)

### GitHub Actions自动发布
创建 `.github/workflows/release.yml`：
```yaml
name: Build and Release

on:
  push:
    tags:
      - 'v*'

jobs:
  build-and-release:
    runs-on: windows-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pyinstaller
    
    - name: Build executable
      run: python build.py
    
    - name: Create Release
      uses: softprops/action-gh-release@v1
      with:
        files: |
          dist/GitCommitTool.exe
          GitCommitTool_Portable.zip
        generate_release_notes: true
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## 🎯 版本管理最佳实践

### 版本号规则
- **主版本号 (Major)**: 重大功能更新或不兼容更改
- **次版本号 (Minor)**: 新功能添加，向下兼容
- **修订号 (Patch)**: 错误修复和小改进

### 下一版本规划
- v1.1: 深色模式支持
- v1.2: 数据统计功能
- v2.0: Web界面版本

---

**🎉 祝你的项目发布成功！** 