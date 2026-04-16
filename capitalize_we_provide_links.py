import os
import re

def capitalize_proper(text):
    # Skip if it's just whitespace or special chars
    if not text.strip() or re.match(r'^[^\w\s]+$', text.strip()):
        return text
        
    words = text.split()
    capitalized_words = []
    # common words to NOT capitalize unless first/last (simplified)
    lower_exceptions = {'and', 'or', 'the', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'with', 'by', 'of'}
    
    for i, word in enumerate(words):
        word_lower = word.lower()
        # Handle acronyms and special cases
        if word_lower in ["seo", "ppc"]:
            capitalized_words.append(word.upper())
        elif word_lower == "ecommerce":
            capitalized_words.append("eCommerce")
        elif word_lower == "us":
            capitalized_words.append("US")
        else:
            # Capitalize if first word, last word, or not an exception
            if i == 0 or i == len(words) - 1 or word_lower not in lower_exceptions:
                if word.islower():
                    capitalized_words.append(word.capitalize())
                else:
                    # Respect existing capitalization
                    capitalized_words.append(word)
            else:
                capitalized_words.append(word_lower)
                
    return " ".join(capitalized_words)

def process_we_provide_links():
    root_dir = r'c:\Users\Administrator\Desktop\tech\tech'
    
    # regex for "We Provide" heading
    header_re = re.compile(r'<h6[^>]*>\s*We Provide\s*</h6>', re.IGNORECASE)
    # regex for <a> tags
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

                    # Find all "We Provide" headings
                    matches = list(header_re.finditer(content))
                    if not matches:
                        continue
                        
                    new_content = content
                    file_links_updated = 0
                    
                    # Work backwards to avoid offset issues
                    for match in reversed(matches):
                        start_pos = match.end()
                        # Look for the next section or h6 or end of file
                        next_h_match = header_re.search(content, start_pos)
                        end_pos = next_h_match.start() if next_h_match else len(content)
                        
                        # Limit range to avoid capturing too much (e.g. 2000 chars)
                        search_range_end = min(start_pos + 2000, end_pos)
                        block = content[start_pos:search_range_end]
                        
                        def replacement(a_match):
                            nonlocal file_links_updated
                            start_tag = a_match.group(1)
                            inner_content = a_match.group(2)
                            end_tag = a_match.group(3)

                            # Capitalize text node parts
                            parts = re.split(r'(<[^>]+>)', inner_content)
                            new_parts = []
                            changed = False
                            for part in parts:
                                if part.startswith('<'):
                                    new_parts.append(part)
                                else:
                                    if part.strip():
                                        capped = capitalize_proper(part)
                                        if capped != part:
                                            changed = True
                                        new_parts.append(capped)
                                    else:
                                        new_parts.append(part)
                            
                            if changed:
                                file_links_updated += 1
                                return start_tag + "".join(new_parts) + end_tag
                            return a_match.group(0)

                        new_block = a_tag_re.sub(replacement, block)
                        new_content = new_content[:start_pos] + new_block + new_content[start_pos + len(block):]

                    if file_links_updated > 0:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        updated_files += 1
                        total_links_updated += file_links_updated
                        print(f"Updated {file_links_updated} links in: {file_path}")
                        
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    print(f"Total files updated: {updated_files}")
    print(f"Total links updated: {total_links_updated}")

if __name__ == "__main__":
    process_we_provide_links()
