import os
import re

def verify_and_fix_css_links():
    root_dir = r'c:\Users\Administrator\Desktop\tech\tech'
    target_files = []
    for root, dirs, files in os.walk(root_dir):
        if 'wp-admin' in root or 'wp-includes' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                target_files.append(os.path.join(root, file))

    missing_links = []
    for file_path in target_files:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Check if mobile-fix.css is linked
        if 'mobile-fix.css' not in content.lower():
            missing_links.append(file_path)
    
    print(f"Found {len(missing_links)} files missing mobile-fix.css link.")
    
    for file_path in missing_links:
        # Determine relative path
        rel_path = os.path.relpath(root_dir, os.path.dirname(file_path))
        if rel_path == '.':
            href = 'mobile-fix.css'
        else:
            href = rel_path.replace('\\', '/') + '/mobile-fix.css'
        
        link_tag = f'\n    <link rel="stylesheet" href="{href}">'
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Inject before </head>
        if '</head>' in content:
            new_content = content.replace('</head>', f'{link_tag}\n</head>')
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected link into {file_path}")
        else:
            print(f"WARNING: Could not find </head> in {file_path}")

if __name__ == "__main__":
    verify_and_fix_css_links()
