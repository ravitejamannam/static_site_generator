from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("Input must be a TextNode")
    
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    
    if text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("LINK type must have a URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    
    if text_node.text_type == TextType.IMAGE:
        if not text_node.url or not text_node.text:
            raise ValueError("IMAGE type must have both src (URL) and alt (text)")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    
    raise ValueError("Unknown TextType")
