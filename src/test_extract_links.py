import unittest
from extract_links import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        expected = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com)"
        expected = [("link", "https://www.example.com")]
        self.assertListEqual(extract_markdown_links(text), expected)

if __name__ == "__main__":
    unittest.main()