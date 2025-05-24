from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from test_htmlnode import TestParentNode
def main():
    dummy = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    node = HTMLNode(props={
        "href": "http://www.google.com",
        "target": "_blank",
    }, tag='h1', value="aaaaaa", children="a" )
    html = node.props_to_html()
    # html2 = LeafNode("text", {"href":"www.example.com"}, "a")
    # print(html)
    # print(html2.to_html())
    TestParentNode.test_to_html_with_multiple_children_with_multiple_grandchildren("")

main()