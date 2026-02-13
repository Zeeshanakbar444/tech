import os

root_dir = r'c:\Users\Administrator\Desktop\tech'

def process_file(filepath):
    rel_root = os.path.relpath(root_dir, os.path.dirname(filepath))
    if rel_root == '.':
        return # Skip root files for this specific fix
    
    rel_root = rel_root.replace('\\', '/') + '/'
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return
    
    changed = False
    
    # Fix logo link - Only if it doesn't already have relative path
    old_link = '<a href="index.html@p=2839.html" class="logo">'
    if old_link in content:
        new_link = f'<a href="{rel_root}index.html@p=2839.html" class="logo">'
        content = content.replace(old_link, new_link)
        changed = True

    # Fix logo image - Target various possible broken forms
    # 1. src="./wp-content/images/..."
    old_img_1 = '<img src="./wp-content/images/us_tech_logo-removebg-preview.png" alt="">'
    if old_img_1 in content:
        new_img_1 = f'<img src="{rel_root}wp-content/images/us_tech_logo-removebg-preview.png" alt="">'
        content = content.replace(old_img_1, new_img_1)
        changed = True
    
    # 2. src="wp-content/images/..." (missing dot)
    old_img_2 = '<img src="wp-content/images/us_tech_logo-removebg-preview.png" alt="">'
    if old_img_2 in content:
        new_img_2 = f'<img src="{rel_root}wp-content/images/us_tech_logo-removebg-preview.png" alt="">'
        content = content.replace(old_img_2, new_img_2)
        changed = True

    if changed:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed header links in {filepath}")
        except Exception as e:
            print(f"Error writing {filepath}: {e}")

if __name__ == "__main__":
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                process_file(os.path.join(root, file))
