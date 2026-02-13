import os

root_dir = r'c:\Users\Administrator\Desktop\tech'
css_filename = 'mobile-fix.css'

def process_html_file(filepath):
    # Calculate relative path to root for the CSS file
    rel_path = os.path.relpath(root_dir, os.path.dirname(filepath))
    if rel_path == '.':
        css_rel_path = css_filename
    else:
        css_rel_path = os.path.join(rel_path, css_filename).replace('\\', '/')
    
    link_tag = f'<link rel="stylesheet" href="{css_rel_path}">'
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    if css_filename in content:
        print(f"Skipping {filepath} (already linked)")
        return

    # Find a good place to insert - after the last stylesheet link or before </head>
    head_end_tag = '</head>'
    if head_end_tag in content:
        new_content = content.replace(head_end_tag, f'    {link_tag}\n{head_end_tag}')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Could not find <head> in {filepath}")

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            process_html_file(filepath)
