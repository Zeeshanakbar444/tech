import os
import re

def titlecase_we_provide():
    root_dir = r'c:\Users\Administrator\Desktop\tech\tech'
    # Regular expression to find "we provide" case-insensitively
    pattern = re.compile(r'\bwe provide\b', re.IGNORECASE)
    
    for root, dirs, files in os.walk(root_dir):
        if 'wp-admin' in root or 'wp-includes' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    # Search and replace
                    new_content, count = pattern.subn('We Provide', content)
                    
                    if count > 0:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated {count} occurrences in {file_path}")
                except Exception as e:
                    print(f"Error reading/writing {file_path}: {e}")

if __name__ == "__main__":
    titlecase_we_provide()
