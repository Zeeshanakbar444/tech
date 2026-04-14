import os
import re

def find_lowercase_links():
    root_dir = r'c:\Users\Administrator\Desktop\tech\tech'
    a_tag_re = re.compile(r'<a\b[^>]*>(.*?)</a>', re.DOTALL | re.IGNORECASE)
    
    lowercase_found = []
    
    for root, dirs, files in os.walk(root_dir):
        if 'wp-admin' in root or 'wp-includes' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                matches = a_tag_re.findall(content)
                for inner in matches:
                    # Strip tags to get actual text
                    text = re.sub(r'<[^>]+>', '', inner).strip()
                    if text and text.islower() and len(text) > 3:
                        # Skip things like "more", "here", etc. if they are common, 
                        # but actually everything should be Proper Case per user.
                        lowercase_found.append((file_path, text))
    
    return lowercase_found

if __name__ == "__main__":
    results = find_lowercase_links()
    if results:
        print(f"Found {len(results)} potential lowercase links:")
        for res in results[:20]: # show first 20
            print(f"{res[0]}: {res[1]}")
    else:
        print("No lowercase links found!")
