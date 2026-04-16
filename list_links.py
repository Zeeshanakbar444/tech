import os
import re

def list_all_we_provide_links():
    root_dir = r'c:\Users\Administrator\Desktop\tech\tech'
    header_re = re.compile(r'<h6[^>]*>.*?We Provide.*?</h6>', re.IGNORECASE)
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
                    
                    for match in header_re.finditer(content):
                        start_pos = match.end()
                        block = content[start_pos:start_pos + 1500]
                        links = a_tag_re.findall(block)
                        for inner in links:
                            text = re.sub(r'<[^>]+>', ' ', inner).strip()
                            # Clean up extra spaces
                            text = ' '.join(text.split())
                            if text:
                                results.append(f"{file_path}: {text}")
                except:
                    pass
    
    # Sort and unique
    results = sorted(list(set(results)))
    
    with open('all_we_provide_links.txt', 'w', encoding='utf-8') as f:
        for r in results:
            f.write(r + '\n')
    print(f"Total links found: {len(results)}")

if __name__ == "__main__":
    list_all_we_provide_links()
