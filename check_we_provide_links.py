import os
import re

def title_case(text):
    # Basic Title Case logic
    exceptions = {'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'from', 'by', 'of', 'in', 'with'}
    words = text.split()
    if not words: return text
    
    new_words = []
    for i, word in enumerate(words):
        word_clean = re.sub(r'[^\w]', '', word).lower()
        if i == 0 or i == len(words) - 1 or word_clean not in exceptions:
            new_words.append(word.capitalize())
        else:
            new_words.append(word.lower())
    return " ".join(new_words)

def check_links_under_we_provide():
    root_dir = r'c:\Users\Administrator\Desktop\tech\tech'
    # Match heading and its following content
    section_pattern = re.compile(r'(<h6[^>]*>.*?We Provide.*?</h6>)(.*?)(?=<h6|<section|</body>|$)', re.IGNORECASE | re.DOTALL)
    a_tag_pattern = re.compile(r'<a\b[^>]*>(.*?)</a>', re.DOTALL | re.IGNORECASE)
    
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
                    
                    for section_match in section_pattern.finditer(content):
                        inner_content = section_match.group(2)
                        links = a_tag_pattern.finditer(inner_content)
                        for link_match in links:
                            link_text_raw = link_match.group(1)
                            # Remove tags to get pure text
                            text_only = re.sub(r'<[^>]+>', '', link_text_raw).strip()
                            if text_only:
                                # Check if it matches Title Case
                                # A simple check: are there any words that start with lowercase (excl. exceptions)
                                words = text_only.split()
                                needs_fix = False
                                for word in words:
                                    if word[0].islower() and len(word) > 3:
                                        needs_fix = True
                                        break
                                if needs_fix:
                                    results.append(f"{file_path}: Potential mismatch: '{text_only}'")
                except:
                    pass
    
    with open('potential_link_issues.txt', 'w', encoding='utf-8') as f:
        for r in results:
            f.write(r + '\n')
    print(f"Check complete. Found {len(results)} potential link issues.")

if __name__ == "__main__":
    check_links_under_we_provide()
