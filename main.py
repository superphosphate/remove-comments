import argparse
import re
from pathlib import Path

# 支持的语言及其注释类型定义
COMMENT_PATTERNS = {
    # 单行注释, 多行注释开始, 多行注释结束
    'python': [r'#.*', r'"""', r'"""', r"'''", r"'''"],
    'javascript': [r'//.*', r'/\*', r'\*/'],
    'java': [r'//.*', r'/\*', r'\*/'],
    'c': [r'//.*', r'/\*', r'\*/'],
    'cpp': [r'//.*', r'/\*', r'\*/'],
    'csharp': [r'//.*', r'/\*', r'\*/'],
    'php': [r'//.*|#.*', r'/\*', r'\*/'],
    'ruby': [r'#.*', r'=begin', r'=end'],
    'html': [r'<!--', r'-->'],
    'css': [r'/\*', r'\*/'],
    'go': [r'//.*', r'/\*', r'\*/'],
    'rust': [r'//.*', r'/\*', r'\*/'],
    'swift': [r'//.*', r'/\*', r'\*/'],
    'shell': [r'#.*'],
    'powershell': [r'#.*', r'<#', r'#>'],
    'sql': [r'--.*', r'/\*', r'\*/'],
    'xml': [r'<!--', r'-->'],
}

# 文件扩展名到语言的映射
FILE_EXTENSIONS = {
    '.py': 'python',
    '.js': 'javascript',
    '.jsx': 'javascript',
    '.ts': 'javascript',
    '.tsx': 'javascript', 
    '.java': 'java',
    '.c': 'c',
    '.h': 'c',
    '.cpp': 'cpp',
    '.hpp': 'cpp',
    '.cc': 'cpp',
    '.cs': 'csharp',
    '.php': 'php',
    '.rb': 'ruby',
    '.html': 'html',
    '.htm': 'html',
    '.css': 'css',
    '.go': 'go',
    '.rs': 'rust',
    '.swift': 'swift',
    '.sh': 'shell',
    '.bash': 'shell',
    '.ps1': 'powershell',
    '.sql': 'sql',
    '.xml': 'xml',
}

def remove_comments_from_file(file_path, output_dir, combined_output=None):
    """处理单个文件，去除注释后输出到指定目录"""
    file_path = Path(file_path)
    extension = file_path.suffix.lower()
    
    # 检查是否支持该文件类型
    if extension not in FILE_EXTENSIONS:
        print(f"不支持的文件类型: {extension}")
        return
    
    language = FILE_EXTENSIONS[extension]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 处理注释
        content_without_comments = remove_comments(content, language)
        
        # 为Java文件添加特殊注释头
        if language == 'java':
            java_header = f"//src/main/java/org/example/{file_path.name}\n"
            content_without_comments = java_header + content_without_comments
        
        # 如果使用合并输出模式
        if combined_output is not None:
            # 添加文件分隔符
            separator = f"\n\n// ---------- {file_path.name} ----------\n\n"
            with open(combined_output, 'a', encoding='utf-8') as f:
                f.write(separator + content_without_comments)
            print(f"已将 {file_path} 添加到合并输出文件")
            return
            
        # 创建输出文件路径
        if output_dir:
            output_path = Path(output_dir) / f"{file_path.stem}_no_comments{file_path.suffix}"
        else:
            output_path = file_path.with_name(f"{file_path.stem}_no_comments{file_path.suffix}")
        
        # 写入输出文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content_without_comments)
        
        print(f"处理完成: {file_path} -> {output_path}")
    
    except Exception as e:
        print(f"处理文件 {file_path} 出错: {str(e)}")

def remove_comments(content, language):
    """根据语言类型去除代码中的注释"""
    if language not in COMMENT_PATTERNS:
        return content
    
    patterns = COMMENT_PATTERNS[language]
    
    # 处理单行注释
    if patterns[0]:
        content = re.sub(patterns[0], '', content)
    
    # 处理多行注释 (如果语言支持)
    if len(patterns) >= 3:  # 存在多行注释模式
        multi_line_start, multi_line_end = patterns[1], patterns[2]
        
        # 使用非贪婪匹配处理多行注释
        pattern = f"{multi_line_start}.*?{multi_line_end}"
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # 处理可能存在的第二种多行注释格式 (如Python的三引号)
        if len(patterns) >= 5:
            multi_line_start2, multi_line_end2 = patterns[3], patterns[4]
            pattern = f"{multi_line_start2}.*?{multi_line_end2}"
            content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # 删除空行
    content = re.sub(r'\n\s*\n', '\n\n', content)
    
    return content

def process_directory(directory, output_dir, recursive=False, combine_output=False):
    """处理目录中的所有支持的代码文件"""
    directory = Path(directory)
    
    if not directory.exists() or not directory.is_dir():
        print(f"目录不存在或不是有效目录: {directory}")
        return
    
    # 确保输出目录存在
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    
    # 获取所有文件
    if recursive:
        files = list(directory.glob('**/*'))
    else:
        files = list(directory.glob('*'))
    
    # 过滤出支持的文件类型
    supported_files = [f for f in files if f.is_file() and f.suffix.lower() in FILE_EXTENSIONS]
    
    if not supported_files:
        print(f"在目录 {directory} 中没有找到支持的文件类型")
        return
    
    # 设置合并输出文件
    combined_output = None
    if combine_output:
        if output_dir:
            combined_output = Path(output_dir) / f"{directory.name}_combined_no_comments.txt"
        else:
            combined_output = directory / f"{directory.name}_combined_no_comments.txt"
        
        # 创建或清空合并输出文件
        with open(combined_output, 'w', encoding='utf-8') as f:
            f.write(f"// 合并来自 {directory} 的所有代码文件\n\n")
    
    # 处理每个文件
    for file_path in supported_files:
        remove_comments_from_file(file_path, output_dir, combined_output)
    
    if combine_output:
        print(f"已将所有文件合并输出到: {combined_output}")

def main():
    parser = argparse.ArgumentParser(description='去除代码文件中的注释')
    parser.add_argument('path', help='要处理的文件或目录路径')
    parser.add_argument('-o', '--output', help='输出文件或目录的路径')
    parser.add_argument('-r', '--recursive', action='store_true', help='递归处理目录')
    parser.add_argument('-c', '--combine', action='store_true', help='将目录下的所有文件合并输出到一个文件中')
    
    args = parser.parse_args()
    
    path = Path(args.path)
    
    if path.is_file():
        remove_comments_from_file(path, args.output)
    elif path.is_dir():
        process_directory(path, args.output, args.recursive, args.combine)
    else:
        print(f"路径不存在或既不是文件也不是目录: {path}")

if __name__ == "__main__":
    main()