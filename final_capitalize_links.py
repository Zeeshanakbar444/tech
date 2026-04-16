import os
import re

def title_case_aggressive(text):
    words = text.split()
    new_words = []
    acronyms = {'SEO', 'PPC', 'US', 'ADA', 'WCAG', 'CMS', 'KPI', 'KPIS'}
    
    for word in words:
        word_clean = re.sub(r'[^\w]', '', word)
        if word_clean.upper() in acronyms:
            new_words.append(word.upper())
        elif word.lower() == "ecommerce":
            new_words.append("ECommerce")
        elif word.lower() == "wordpress":
            new_words.append("WordPress")
        else:
            if len(word) > 1:
                # Proper Case: Capitalize first letter, keep rest as is if there's mixed case (like iPhone)
                # But here we probably want to normalize to Capitalized.
                new_words.append(word[0].upper() + word[1:])
            else:
                new_words.append(word.upper())
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
                    if not matches:
                        continue
                        
                    new_content = content
                    file_links_updated = 0
                    
                    # We will process each block and rebuild the content
                    # Start from the last match and go backwards
                    for match in reversed(matches):
                        start_pos = match.end()
                        # Find the next h6 or next section or end of file
                        # Looking at the HTML, sections are often separated by </div> or </section>
                        # We'll look for the next </section> or </div> that seems to end the container
                        # But to be safe and "quick", we'll just take the next 3000 chars and find the </ul>
                        next_ul_end = content.find('</ul>', start_pos)
                        if next_ul_end == -1:
                            end_pos = min(start_pos + 3000, len(content))
                        else:
                            end_pos = next_ul_end + 5
                        
                        block = new_content[start_pos:end_pos]
                        
                        def a_replacement(a_match):
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

                        new_block = a_tag_re.sub(a_replacement, block)
                        # Replace the block in new_content
                        new_content = new_content[:start_pos] + new_block + new_content[end_pos:]

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
