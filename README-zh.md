# 🚀 代码注释清理工具

**一键去除代码注释，保持代码纯净！** 

喜欢这个项目的话，请给一个 ⭐️ 吧！

## 🔍 项目简介

这个强大的Python脚本能够智能识别并移除多种编程语言文件中的注释，让你的代码更加简洁干净。支持Python、JavaScript、Java、C/C++、C#、PHP等多种流行语言！Pylint测试9.67/10.0

## ✨ 核心功能

- 🎯 **多语言支持** - 自动识别多种编程语言
- 📝 **智能注释移除** - 精准处理单行和多行注释
- 📂 **批量处理** - 支持单个文件或整个目录
- 🔁 **递归操作** - 可选项处理嵌套目录结构
- 🧩 **合并输出** - 将多个文件合并为单一输出文件
- � **特殊处理** - 为Java文件添加规范的注释头

## 🛠️ 快速开始

### 安装要求
```bash
pip install -r requirements.txt
```

### 使用方式

#### 处理单个文件
```bash
python main.py path/to/file.py -o output_directory
```

#### 处理整个目录
```bash
python main.py path/to/directory -o output_directory
```

#### 递归处理目录（包括子目录）
```bash
python main.py path/to/directory -o output_directory -r
```

#### 合并目录下所有文件
```bash
python main.py path/to/directory -o output_directory -c
```

#### 递归合并所有文件
```bash
python main.py path/to/directory -o output_directory -r -c
```

## 🌟 高级特性

- **智能文件识别**：自动根据扩展名确定文件类型
- **保留原始结构**：输出文件添加"_no_comments"后缀
- **特殊注释处理**：Java文件自动添加规范路径注释头
- **自定义扩展**：轻松添加对新语言的支持

## 📂 输出示例

```
原始文件结构：
src/
  ├── main.py
  └── utils/
      ├── helper.js
      └── config.php

处理后结构：
output/
  ├── main_no_comments.py
  └── utils/
      ├── helper.js
      ├── config.php
      ├── helper_no_comments.txt
      └── config_no_comments.txt
```

## 🛠️ 自定义配置

如需支持其他语言，可编辑脚本中的：
- `COMMENT_PATTERNS` - 添加新语言的注释模式
- `FILE_EXTENSIONS` - 扩展名与语言映射

## 📅 开发路线

- [ ] 增强特殊注释头功能（支持更多路径模式）
- [ ] 添加对更多语言的支持
- [ ] 实现注释统计功能
- [ ] 开发GUI界面版本

## 🤝 贡献指南

欢迎提交PR或Issue！让我们一起打造更强大的代码清理工具！

## 📜 许可证

AGPL 3.0

---

**立即体验清爽的无注释代码世界！** 🎉