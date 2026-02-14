import os
import re

root_dir = r'C:\Users\Administrator\Desktop\tech'

def fix_links(filepath):
    # Calculate depth relative to root_dir
    rel_path = os.path.relpath(filepath, root_dir)
    depth = rel_path.count(os.sep)
    
    if depth == 0:
        return # Skip root files
    
    prefix = '../' * depth
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    changed = False
    
    # regex to find href and src attributes
    # We want to match links that don't start with:
    # - http/https
    # - / (absolute)
    # - # (anchor)
    # - tel:
    # - mailto:
    # - ../ (already relative/fixed)
    # - javascript:
    
    def replacement(match):
        attr = match.group(1) # href or src
        quote = match.group(2) # " or '
        link = match.group(3)
        
        # Check if the link should be fixed
        if (re.match(r'^(https?://|/|#|tel:|mailto:|javascript:|\.\./)', link) or 
            link == "" or link == "."):
            return match.group(0)
        
        # Special case: if it starts with ./ just remove it and add prefix
        if link.startswith('./'):
            link = link[2:]
            
        print(f"  Fixing {attr}={quote}{match.group(3)}{quote} -> {prefix}{link}")
        return f'{attr}={quote}{prefix}{link}{quote}'

    # Pattern for href="..." and src="..."
    pattern = r'(href|src)=([\'"])(.*?)\2'
    
    new_content = re.sub(pattern, replacement, content)
    
    if new_content != content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed links in {filepath} (depth {depth})")
            return True
        except Exception as e:
            print(f"Error writing {filepath}: {e}")
            
    return False

if __name__ == "__main__":
    count = 0
    for root, dirs, files in os.walk(root_dir):
        # Skip some directories if necessary
        if '.git' in dirs:
            dirs.remove('.git')
        if 'wp-content' in dirs: # Assets usually don't need link fixing inside themselves
            pass 
            
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                if fix_links(filepath):
                    count += 1
                    
    print(f"Total files fixed: {count}")
