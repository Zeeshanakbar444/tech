import os
import re

def title_case_aggressive(text):
    # This one will capitalize EVERY word, no exceptions for common small words
    # because the user wants "Proper Case" for these specific link titles.
    words = text.split()
    new_words = []
    for word in words:
        # Special case: if it's already uppercase (like SEO), keep it
        if word.isupper() and len(word) > 1:
            new_words.append(word)
        # eCommerce -> Ecommerce (if user wants Proper Case)
        elif word.startswith('e') and len(word) > 1 and word[1].isupper():
            new_words.append(word.capitalize())
        else:
            new_words.append(word.capitalize())
    return " ".join(new_words)

def process_we_provide_links():
    root_dir = r'c:\Users\Administrator\Desktop\tech\tech'
    header_re = re.compile(r'<h6[^>]*>.*?We Provide.*?</h6>', re.IGNORECASE)
    a_tag_re = re.compile(r'(<a\b[^>]*>)(.*?)(</a>)', re.DOTALL | re.IGNORECASE)

    updated_files = 0
    total_links_updated = 0
    
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
                    if not matches: continue
                    
                    new_content = content
                    file_links_updated = 0
                    
                    for match in reversed(matches):
                        start_pos = match.end()
                        block_end = min(start_pos + 1500, len(content))
                        block = content[start_pos:block_end]
                        
                        def replacement(a_match):
                            nonlocal file_links_updated
                            start_tag = a_match.group(1)
                            inner_content = a_match.group(2)
                            end_tag = a_match.group(3)

                            parts = re.split(r'(<[^>]+>)', inner_content)
                            new_parts = []
                            changed = False
                            for part in parts:
                                if part.startswith('<'):
                                    new_parts.append(part)
                                else:
                                    if part.strip():
                                        capped = title_case_aggressive(part)
                                        if capped != part:
                                            changed = True
                                        new_parts.append(capped)
                                    else:
                                        new_parts.append(part)
                            
                            if changed:
                                file_links_updated += 1
                                return start_tag + "".join(new_parts) + end_tag
                            return a_match.group(0)

                        new_block = a_tag_pattern.sub(replacement, block) # Wait, a_tag_pattern is a mistake, should be a_tag_re
                        # I'll fix this in the next call
