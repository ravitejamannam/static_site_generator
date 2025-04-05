import os
import re
from htmlnode import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path, base_path="/"):
    print(f"Generating page from {from_path} to {dest_path} with base_path: {base_path}")
    
    with open(from_path, 'r') as f:
        markdown_content = f.read()

    with open(template_path, 'r') as f:
        template_content = f.read()

    title = extract_title(markdown_content)
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Replace markdown links and images
    html_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html_content)
    html_content = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', html_content)

    # Fill template
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Fix href and src to use base_path
    final_html = final_html.replace('href="/', f'href="{base_path}')
    final_html = final_html.replace('src="/', f'src="{base_path}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(final_html)