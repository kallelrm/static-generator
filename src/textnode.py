from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def text_to_html_node(self):
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(tag=None, value=self.text)
            case TextType.BOLD:
                return LeafNode("b", self.text)
            case TextType.ITALIC:
                return LeafNode("i", self.text)
            case TextType.CODE:
                return LeafNode("code", self.text)
            case TextType.LINK:
                return LeafNode("a", self.text, None, {"href": f"{self.url}"})
            case TextType.IMAGE:
                return LeafNode("img", "", None, {"src": f"{self.url}", "alt": f"{self.text}"})
            case _:
                raise Exception()

    
    def __eq__(self, target):
        if (self.text == target.text and self.text_type.value == target.text_type.value and self.url == target.url):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"