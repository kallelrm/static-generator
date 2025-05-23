from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    node = HTMLNode(props={
        "href": "http://www.google.com",
        "target": "_blank",
    }, tag='h1', value="aaaaaa", children="a" )
    html = node.props_to_html()
    print(html)
    print(node)

main()