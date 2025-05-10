# Remove Comments 

If you like it, please give a "⭐️"!

This script can read various common code files and output the content without comments to a new text file.  

> I am currently still actively learning English and have utilized advanced AI translation technology for the English sections of the project documentation. However, please note that the Chinese version remains the authoritative version for all content. I apologize for any inconvenience this may cause and sincerely thank you for your understanding and cooperation.

## Usage  

1. **Process a Single File**:  
   ```bash  
   python main.py <file_path> -o <output_directory>  
   ```  

2. **Process an Entire Directory**:  
   ```bash  
   python main.py <directory_path> -o <output_directory>  
   ```  

3. **Process Directory Recursively**:  
   ```bash  
   python main.py <directory_path> -o <output_directory> -r  
   ```  

4. **Merge All Files in a Directory into a Single Output File**:  
   ```bash  
   python main.py <directory_path> -o <output_directory> -c  
   ```  

5. **Process Recursively and Merge All Files**:  
   ```bash  
   python main.py <directory_path> -o <output_directory> -r -c  
   ```  

## Features  

- Supports multiple common programming languages, including Python, JavaScript, Java, C/C++, C#, PHP, etc.  
- Detects and removes both single-line and multi-line comments  
- Supports recursive directory processing  
- Preserves the original file structure, appending "_no_comments" to output filenames  
- Handles edge cases, such as comment symbols within strings  
- Automatically adds a special comment header `//src/main/java/org/example/{fileName}` for Java files  
- Provides an option to merge all files in a directory into a single output file  

To support additional languages or file types, you can add corresponding definitions in the `COMMENT_PATTERNS` and `FILE_EXTENSIONS` dictionaries.  

## TODO  

1. Enhance language support for advanced special comment headers like `//src/main/java/{org}/{pattern}/{fileName}`  
...
