# ⚙️ 配置文件管理指南

## 📋 配置文件结构

本项目采用模板化配置管理，确保个人配置不会意外上传到版本控制系统：

```
📁 项目根目录
├── 📄 config.template.yaml  ✅ 模板文件 (版本控制)
├── 📄 config.yaml          ❌ 个人配置 (被gitignore忽略)
└── 📄 .gitignore           ✅ 包含config.yaml忽略规则
```

## 🔄 配置文件工作流程

### 1. 首次使用
程序会自动检测并创建配置文件：

```bash
# 首次运行
python gui.py

# 程序输出:
⚠️ 配置文件 config.yaml 不存在
📋 正在从模板 config.template.yaml 创建配置文件...
✅ 已创建配置文件: config.yaml
💡 请编辑 config.yaml 文件设置你的个人配置
```

### 2. 手动创建 (可选)
```bash
# 复制模板文件
cp config.template.yaml config.yaml

# 或者 Windows
copy config.template.yaml config.yaml
```

### 3. 个性化配置
编辑 `config.yaml` 文件，设置你的个人配置：

```yaml
# 修改为你的实际配置
root_directory: "D:\\MyProjects"
author: "你的Git用户名"
output_directory: "D:\\Documents\\GitLogs"
```

## 🚫 版本控制策略

### 被忽略的文件 (.gitignore)
```bash
# 个人配置文件 - 不上传到仓库
config.yaml

# 临时文件
git_commits_*.txt
config_backup.yaml
```

### 被版本控制的文件
```bash
# 模板文件 - 会上传到仓库，供其他用户参考
config.template.yaml

# 代码文件
gui.py
git_commit_tool.py
# ... 其他源码文件
```

## 🔧 开发者更新配置模板

### 添加新配置项
当需要添加新功能的配置项时：

1. **更新模板文件**
   ```yaml
   # 在 config.template.yaml 中添加新配置项
   new_feature_enabled: false    # 新功能开关 (true/false)
                                # 描述新功能的作用和用法
   ```

2. **更新默认值**
   ```python
   # 在 git_commit_tool.py 的 load_config 函数中添加默认值
   return {
       'root_directory': '',
       'author': '',
       # ... 现有配置
       'new_feature_enabled': False,  # 新增配置项默认值
   }
   ```

3. **更新文档**
   - 在 `USAGE.md` 中说明新配置项的用法
   - 在 `README.md` 中更新功能列表

### 修改配置项说明
直接编辑 `config.template.yaml` 文件中的注释：

```yaml
# 更新注释，提供更详细的说明
root_directory: "C:\\workspace"    # Git仓库根目录 (必填)
                                  # 💡 新增: 支持相对路径，如 "./projects"
                                  # 示例: "C:\\workspace" 或 "/home/user/projects"
```

## 📚 用户使用指南

### 配置文件丢失怎么办？
```bash
# 方法1: 重新运行程序，自动从模板创建
python gui.py

# 方法2: 手动复制模板
cp config.template.yaml config.yaml
```

### 配置项不生效怎么办？
1. **检查YAML语法**
   ```bash
   # 使用在线YAML验证器检查语法
   # 或者使用Python验证
   python -c "import yaml; yaml.safe_load(open('config.yaml'))"
   ```

2. **检查配置项拼写**
   - 参考 `config.template.yaml` 中的正确拼写
   - 注意大小写敏感

3. **重置配置文件**
   ```bash
   # 备份当前配置
   cp config.yaml config.backup.yaml
   
   # 重新创建
   rm config.yaml
   cp config.template.yaml config.yaml
   ```

### 备份和恢复配置
```bash
# 备份配置
cp config.yaml config.backup.yaml

# 恢复配置
cp config.backup.yaml config.yaml
```

## 🔄 团队协作最佳实践

### 项目维护者
- ✅ 更新 `config.template.yaml` 模板
- ✅ 在文档中说明新配置项
- ✅ 确保 `config.yaml` 在 `.gitignore` 中
- ❌ 不要提交个人的 `config.yaml` 文件

### 项目用户
- ✅ 使用 `config.template.yaml` 创建个人配置
- ✅ 根据需要修改个人配置
- ❌ 不要修改 `config.template.yaml` 文件
- ❌ 不要尝试提交 `config.yaml` 文件

### 多环境配置
```bash
# 开发环境
config.dev.yaml

# 生产环境  
config.prod.yaml

# 测试环境
config.test.yaml

# 在程序中指定配置文件
python main.py --config config.dev.yaml
```

## 🐛 常见问题

### Q: 为什么不直接版本控制config.yaml？
**A:** 防止个人配置（如本地路径、个人信息）泄露到版本控制系统中。

### Q: 如何同步团队配置更新？
**A:** 
1. 拉取最新的 `config.template.yaml`
2. 对比自己的 `config.yaml` 文件
3. 手动添加新的配置项

### Q: 可以自动同步配置更新吗？
**A:** 可以，但需要小心处理：
```bash
# 合并模板更新到个人配置 (高级用户)
# 这会保留你的个人设置，但添加新的配置项
python tools/merge_config.py
```

---

**💡 记住：模板文件是公共的，配置文件是私人的！** 