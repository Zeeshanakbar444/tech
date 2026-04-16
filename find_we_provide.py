import os
import re

def find_we_provide():
    root_dir = r'c:\Users\Administrator\Desktop\tech\tech'
    pattern = re.compile(r'we provide', re.IGNORECASE)
    results = []
    
    for root, dirs, files in os.walk(root_dir):
        if 'wp-admin' in root or 'wp-includes' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            if pattern.search(line):
                                results.append(f"{file_path}:{i+1}: {line.strip()}")
                except Exception as e:
                    results.append(f"Error reading {file_path}: {e}")
    
    with open('find_we_provide_results.txt', 'w', encoding='utf-8') as f:
        for result in results:
            f.write(result + '\n')

if __name__ == "__main__":
    find_we_provide()
