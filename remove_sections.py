import sys

# Read the file
file_path = r"c:/Users/Administrator/Downloads/us tech updated (1) (1)/us tech updated (1)/contact.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find and remove the "BEEN THERE, DEVELOPED THAT" section
# It starts with the comment we added and should end before the next section
start_marker = "<!-- SECTION REMOVED: BEEN THERE, DEVELOPED THAT"
# Find where this section ends - look for the closing </section> tag before the next section starts
section_4_start = content.find(start_marker)

if section_4_start != -1:
    # Find the end of this section (the </section> tag before section--5 starts)
    # Look for "m-section--5" to find where the next section begins
    section_5_start_marker = '<section  class="m-section waypoint m-section--5'
    section_5_pos = content.find(section_5_start_marker, section_4_start)
    
    if section_5_pos != -1:
        # Now find the </section> tag just before section_5_pos
        section_4_end = content.rfind('</section>', section_4_start, section_5_pos)
        
        if section_4_end != -1:
            # Remove section 4
            section_4_end += len('</section>')  # Include the closing tag
            content = content[:section_4_start] + content[section_4_end:]
            print(f"Removed 'BEEN THERE, DEVELOPED THAT' section ({section_4_end - section_4_start} characters)")

# Now find and remove the "DAILY DIGITAL DOSE" section
# It's in m-section--5
section_5_start_marker = '<section  class="m-section waypoint m-section--5'
section_5_start = content.find(section_5_start_marker)

if section_5_start != -1:
    # Find the end of this section
    # Look for the next <section after this one
    next_section_pos = content.find('<section', section_5_start + 100)
    
    if next_section_pos != -1:
        # Find the </section> tag just before the next section
        section_5_end = content.rfind('</section>', section_5_start, next_section_pos)
        
        if section_5_end != -1:
            section_5_end += len('</section>')  # Include the closing tag
            content = content[:section_5_start] + content[section_5_end:]
            print(f"Removed 'DAILY DIGITAL DOSE' section ({section_5_end - section_5_start} characters)")

# Write the modified content back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully removed both case study sections from contact.html")
