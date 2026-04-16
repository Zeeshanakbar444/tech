import os
import re

def find_lowercase_under_we_provide():
    root_dir = r'c:\Users\Administrator\Desktop\tech\tech'
    header_re = re.compile(r'<h6[^>]*>\s*We Provide\s*</h6>', re.IGNORECASE)
    a_tag_re = re.compile(r'<a\b[^>]*>(.*?)</a>', re.DOTALL | re.IGNORECASE)
    
    results = []
    
    for root, dirs, files in os.walk(root_dir):
        if 'wp-admin' in root or 'wp-includes' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    matches = list(header_re.finditer(content))
                    for match in matches:
                        start_pos = match.end()
                        # search next 1500 chars for links
                        block = content[start_pos:start_pos + 1500]
                        links = a_tag_re.findall(block)
                        for inner in links:
                            # Strip tags to get text
                            text = re.sub(r'<[^>]+>', '', inner).strip()
                            if text and text.islower():
                                results.append(f"{file_path}: Found lowercase link: '{text}'")
                except:
                    pass
                    
    with open('lowercase_links_diagnostic.txt', 'w', encoding='utf-8') as f:
        for r in results:
            f.write(r + '\n')
    print(f"Diagnostics complete. Found {len(results)} potential issues.")

if __name__ == "__main__":
    find_lowercase_under_we_provide()
