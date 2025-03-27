def markdown_to_blocks(markdown):
    # Split markdown by double newlines and strip each block
    blocks = [block.strip() for block in markdown.split("\n\n")]
    
    # Remove empty blocks
    return [block for block in blocks if block]