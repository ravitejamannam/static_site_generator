# src/extract_title.py

def extract_title(markdown):
    """
    Extracts the h1 header from a markdown string.
    
    Args:
        markdown (str): The markdown text to parse
        
    Returns:
        str: The title without the leading '# ' and any whitespace
        
    Raises:
        Exception: If no h1 header is found
    """
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception("No h1 header found in markdown")