import re

def extract_markdown_images(text):
    """Extracts image alt text and URLs from Markdown."""
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    """Extracts anchor text and URLs from Markdown links."""
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)