import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_equal_different_text(self):
        node1 = TextNode("This is text", TextType.BOLD)
        node2 = TextNode("This is another text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_different_type(self):
        node1 = TextNode("Some text", TextType.BOLD)
        node2 = TextNode("Some text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_equal_with_url(self):
        node1 = TextNode("Click here", TextType.LINK, "https://example.com")
        node2 = TextNode("Click here", TextType.LINK, "https://example.com")
        self.assertEqual(node1, node2)

    def test_not_equal_different_url(self):
        node1 = TextNode("Click here", TextType.LINK, "https://example.com")
        node2 = TextNode("Click here", TextType.LINK, "https://another.com")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()