# 去除代码注释脚本

喜欢这个项目的话，请给一个“⭐️”吧！

该脚本能够读取各种常见代码文件，并输出去掉注释后的内容到新的文本文件中。

## 使用方法

1. **处理单个文件**：
   ```dash
   python main.py <文件路径> -o <输出目录>
   ```

2. **处理整个目录**：
   ```dash
   python main.py <目录路径> -o <输出目录>
   ```

3. **递归处理目录**：
   ```dash
   python main.py <目录路径> -o <输出目录> -r
   ```

4. **合并目录下所有文件到单一输出文件**：
   ```dash
   python main.py <目录路径> -o <输出目录> -c
   ```

5. **递归处理并合并所有文件**：
   ```dash
   python main.py <目录路径> -o <输出目录> -r -c
   ```

## 功能特点

- 支持多种常见编程语言，包括 Python、JavaScript、Java、C/C++、C#、PHP 等
- 识别并移除单行注释和多行注释
- 支持递归处理目录
- 保留原始文件结构，输出文件名添加 "_no_comments" 后缀
- 处理特殊情况，如字符串中的注释符号
- 为Java文件自动添加特殊注释头 `//src/main/java/org/example/{fileName}`
- 提供将目录下所有文件合并到单一输出文件的选项

如果需要支持其他语言或文件类型，可以在 `COMMENT_PATTERNS` 和 `FILE_EXTENSIONS` 字典中添加相应的定义。

## TODO

1. 为语言支持更高级的特殊注释头 `//src/main/java/{org}/{patten}/{fileName}`
...