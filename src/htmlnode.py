class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        if self.tag is None:
            return self.value or ""
        children_html = "".join(child.to_html() for child in self.children)
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"

    def props_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={len(self.children) if self.children else 0}, props={self.props})"


def markdown_to_html_node(markdown):
    def split_blocks(md):
        return [block.strip() for block in md.strip().split("\n\n")]

    def determine_block_type(block):
        if block.startswith("```"):
            return "code"
        elif block.startswith(">"):
            return "quote"
        elif block.startswith("#"):
            return "heading"
        elif block.startswith("- ") or block.startswith("* "):
            return "ul"
        elif block[0].isdigit() and block[1] == ".":
            return "ol"
        else:
            return "paragraph"

    def text_to_children(text):
        # Inline markdown parsing for bold, italic, and code
        children = []
        while text:
            if "**" in text:
                before, _, rest = text.partition("**")
                if before:
                    children.append(HTMLNode(value=before))
                bold_text, _, text = rest.partition("**")
                children.append(HTMLNode(tag="b", children=[HTMLNode(value=bold_text)]))
            elif "_" in text:
                before, _, rest = text.partition("_")
                if before:
                    children.append(HTMLNode(value=before))
                italic_text, _, text = rest.partition("_")
                children.append(HTMLNode(tag="i", children=[HTMLNode(value=italic_text)]))
            elif "`" in text:
                before, _, rest = text.partition("`")
                if before:
                    children.append(HTMLNode(value=before))
                code_text, _, text = rest.partition("`")
                children.append(HTMLNode(tag="code", children=[HTMLNode(value=code_text)]))
            else:
                children.append(HTMLNode(value=text))
                break
        return children

    def parse_block(block):
        block_type = determine_block_type(block)
        if block_type == "code":
            code_content = block.strip("```")
            return HTMLNode(tag="pre", children=[HTMLNode(tag="code", value=code_content)])
        elif block_type == "quote":
            quote_content = block.lstrip(">").strip()
            return HTMLNode(tag="blockquote", children=text_to_children(quote_content))
        elif block_type == "heading":
            level = block.count("#", 0, block.find(" "))
            heading_content = block.lstrip("#").strip()
            return HTMLNode(tag=f"h{level}", children=text_to_children(heading_content))
        elif block_type == "ul":
            items = block.split("\n")
            children = [HTMLNode(tag="li", children=text_to_children(item.lstrip("-* ").strip())) for item in items]
            return HTMLNode(tag="ul", children=children)
        elif block_type == "ol":
            items = block.split("\n")
            children = [HTMLNode(tag="li", children=text_to_children(item.lstrip("0123456789. ").strip())) for item in items]
            return HTMLNode(tag="ol", children=children)
        else:  # paragraph
            return HTMLNode(tag="p", children=text_to_children(block))

    blocks = split_blocks(markdown)
    children = [parse_block(block) for block in blocks]
    return HTMLNode(tag="div", children=children)