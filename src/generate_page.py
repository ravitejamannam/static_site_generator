# src/generate_page.py
import os
import re
from htmlnode import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    """
    Generates an HTML page from a markdown file using a template.
    
    Args:
        from_path (str): Path to the markdown file
        template_path (str): Path to the HTML template
        dest_path (str): Path where the generated HTML file will be saved
    """
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown file
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    # Read the template file
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Extract the title
    title = extract_title(markdown_content)
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Direct replacement of remaining markdown-style links with HTML links in the final HTML
    html_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html_content)
    
    # Direct replacement of markdown-style images with HTML images in the final HTML
    html_content = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', html_content)
    
    # Replace placeholders in the template
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    # Create destination directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the final HTML to the destination file
    with open(dest_path, 'w') as f:
        f.write(final_html)