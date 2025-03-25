from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if not children or not isinstance(children, list):
            raise ValueError("ParentNode must have a list of children")
        
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        props_str = self.props_to_html()
        children_html = "".join(child.to_html() for child in self.children)

        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"