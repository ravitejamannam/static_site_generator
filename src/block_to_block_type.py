import re
from block_type import BlockType

def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    # Check for Heading (starts with 1-6 # followed by a space)
    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING

    # Check for Code Block (starts and ends with ```)
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Check for Quote Block (every line starts with "> ")
    if all(line.startswith("> ") for line in lines):
        return BlockType.QUOTE

    # Check for Unordered List (every line starts with "- ")
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Check for Ordered List (each line starts with "1. ", "2. ", "3. ", etc.)
    if all(re.match(r"^\d+\. ", line) for line in lines):
        return BlockType.ORDERED_LIST

    # Default to Paragraph
    return BlockType.PARAGRAPH