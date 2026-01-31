from bs4 import BeautifulSoup

# File path to your HTML file
file_path = './index.html'

# Read the file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all anchor tags and replace href with "#"
for a_tag in soup.find_all('a', href=True):
    a_tag['href'] = '#'

# Save the modified HTML back to the file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("✅ All anchor links replaced with '#' successfully.")
