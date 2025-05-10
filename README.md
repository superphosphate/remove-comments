# 🚀 Code Comment Cleaner Tool  

**Remove code comments with one click, keeping your code clean!**  

If you like this project, please give it a ⭐️!  

## 🔍 Project Introduction  

This powerful Python script intelligently identifies and removes comments from various programming language files, making your code cleaner and more concise. It supports popular languages like Python, JavaScript, Java, C/C++, C#, PHP, and more! And it win a 9.67/10.0 Pylint mark. 

## ✨ Core Features  

- 🎯 **Multi-language Support** – Automatically recognizes multiple programming languages  
- 📝 **Smart Comment Removal** – Accurately handles single-line and multi-line comments  
- 📂 **Batch Processing** – Supports single files or entire directories  
- 🔁 **Recursive Operation** – Optional handling of nested directory structures  
- 🧩 **Merged Output** – Combines multiple files into a single output file  
- ✨ **Special Handling** – Adds standardized comment headers for Java files  

## 🛠️ Quick Start  

### Installation Requirements  
```bash  
pip install -r requirements.txt  
```  

### Usage  

#### Process a Single File  
```bash  
python main.py path/to/file.py -o output_directory  
```  

#### Process an Entire Directory  
```bash  
python main.py path/to/directory -o output_directory  
```  

#### Recursively Process a Directory (Including Subdirectories)  
```bash  
python main.py path/to/directory -o output_directory -r  
```  

#### Merge All Files in a Directory  
```bash  
python main.py path/to/directory -o output_directory -c  
```  

#### Recursively Merge All Files  
```bash  
python main.py path/to/directory -o output_directory -r -c  
```  

## 🌟 Advanced Features  

- **Smart File Recognition**: Automatically determines file type based on extension  
- **Preserves Original Structure**: Output files are appended with "_no_comments"  
- **Special Comment Handling**: Java files automatically receive standardized path comment headers  
- **Custom Extensions**: Easily add support for new languages  

## 📂 Output Example  

```
Original file structure:  
src/  
  ├── main.py  
  └── utils/  
      ├── helper.js  
      └── config.php  

Processed structure:  
output/  
  ├── main_no_comments.py  
  └── utils/  
      ├── helper.js  
      ├── config.php  
      ├── helper_no_comments.txt  
      └── config_no_comments.txt  
```  

## 🛠️ Custom Configuration  

To support additional languages, edit the following in the script:  
- `COMMENT_PATTERNS` – Add comment patterns for new languages  
- `FILE_EXTENSIONS` – Map file extensions to languages  

## 📅 Development Roadmap  

- [ ] Enhance special comment header functionality (support more path patterns)  
- [ ] Add support for more languages  
- [ ] Implement comment statistics feature  
- [ ] Develop a GUI version  

## 🤝 Contribution Guidelines  

PRs and Issues are welcome! Let’s build a more powerful code-cleaning tool together!  

## 📜 License  

AGPL 3.0  

---  

**Experience the refreshing world of comment-free code today!** 🎉  
