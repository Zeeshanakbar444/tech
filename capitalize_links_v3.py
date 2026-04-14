import os
import re

def capitalize_proper(text):
    # Handle already capitalized or mixed case words
    words = text.split()
    capitalized_words = []
    for word in words:
        if word.lower() == "seo" or word.lower() == "ppc":
            capitalized_words.append(word.upper())
        elif word.lower() == "ecommerce":
            capitalized_words.append("eCommerce")
        elif word.lower() == "us":
            capitalized_words.append("US")
        else:
            # Capitalize first letter, keep rest as is if there's existing capitalization
            # But the user wants "Proper Case", so usually it's Capitalized.
            # If it's all lowercase, capitalize it.
            if word.islower():
                capitalized_words.append(word.capitalize())
            else:
                # If there's an apostrophe, e.g., "let's" -> "Let's"
                if "'" in word:
                    parts = word.split("'")
                    capitalized_parts = [p.capitalize() if p.islower() else p for p in parts]
                    capitalized_words.append("'".join(capitalized_parts))
                else:
                    capitalized_words.append(word)
    return " ".join(capitalized_words)

def process_html_files():
    root_dir = r'c:\Users\Administrator\Desktop\tech\tech'
    target_files = []
    for root, dirs, files in os.walk(root_dir):
        if 'wp-admin' in root or 'wp-includes' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                target_files.append(os.path.join(root, file))

    # Regex to find <a> tags and their content
    # Matches <a ...>text</a>, handles multi-line and nested tags by capturing until the first </a>
    # We use a non-greedy match for the content: (.*?)
    a_tag_re = re.compile(r'(<a\b[^>]*>)(.*?)(</a>)', re.DOTALL | re.IGNORECASE)

    for file_path in target_files:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        def replacement(match):
            start_tag = match.group(1)
            inner_content = match.group(2)
            end_tag = match.group(3)

            # skip if content contains images or svgs or icons
            if '<img' in inner_content.lower() or '<svg' in inner_content.lower() or '<i' in inner_content.lower():
                # We might still want to capitalize text NEXT to these tags
                # Let's split by tags and capitalize the text parts
                parts = re.split(r'(<[^>]+>)', inner_content)
                new_parts = []
                for part in parts:
                    if part.startswith('<'):
                        new_parts.append(part)
                    else:
                        # This is text
                        if part.strip():
                            new_parts.append(capitalize_proper(part))
                        else:
                            new_parts.append(part)
                return start_tag + "".join(new_parts) + end_tag
            
            if not inner_content.strip():
                return match.group(0)
            
            return start_tag + capitalize_proper(inner_content) + end_tag

        new_content = a_tag_re.sub(replacement, content)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_path}")

if __name__ == "__main__":
    process_html_files()
