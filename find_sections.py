
import re
import os

files = [
    r"c:/Users/Administrator/Downloads/us tech updated (1) (1)/us tech updated (1)/contact.html",
    r"c:/Users/Administrator/Downloads/us tech updated (1) (1)/us tech updated (1)/index.html"
]

for file_path in files:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
        
    print(f"Scanning {os.path.basename(file_path)}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Look for "Web Design" and "Learn More" within reasonable distance
        # or just look for the text
        
        targets = ["Web Design", "Branding", "Web Development"]
        
        for target in targets:
            indices = [m.start() for m in re.finditer(re.escape(target), content, re.IGNORECASE)]
            for i in indices:
                # extracted context
                start = max(0, i - 200)
                end = min(len(content), i + 500)
                snippet = content[start:end]
                
                if "Learn More" in snippet or "learn more" in snippet.lower():
                    print(f"MATCH FOUND in {os.path.basename(file_path)} for '{target}':")
                    print(f"Line approx: {content[:i].count('\\n') + 1}")
                    print("-" * 40)
                    print(snippet)
                    print("-" * 40)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
