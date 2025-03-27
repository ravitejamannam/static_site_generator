import unittest
from block_to_block_type import block_to_block_type
from block_type import BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Subheading"), BlockType.HEADING)

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\nprint('Hello')\n```"), BlockType.CODE)

    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> This is a quote\n> Another line"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. Item 1\n2. Item 2\n3. Item 3"), BlockType.ORDERED_LIST)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph of text."), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()