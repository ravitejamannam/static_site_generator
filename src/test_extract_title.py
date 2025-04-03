import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
    
    def test_title_with_whitespace(self):
        self.assertEqual(extract_title("#    Title with spaces    "), "Title with spaces")
    
    def test_title_with_markdown(self):
        self.assertEqual(extract_title("# Title with **bold** and *italic*"), "Title with **bold** and *italic*")
    
    def test_first_h1_only(self):
        self.assertEqual(extract_title("# First Title\n## Second Title\n# Another H1"), "First Title")
    
    def test_title_not_at_beginning(self):
        self.assertEqual(extract_title("Some text\n\n# The Title"), "The Title")
    
    def test_no_title(self):
        with self.assertRaises(Exception):
            extract_title("No title here\nJust some text")
    
    def test_h2_not_h1(self):
        with self.assertRaises(Exception):
            extract_title("## This is h2, not h1")

if __name__ == '__main__':
    unittest.main()