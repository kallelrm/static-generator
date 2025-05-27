from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from splitter import split_nodes_delimiter
from test_htmlnode import TestParentNode
def main():
    dummy = TextNode("`This` is CODE TEXTO ", TextType.CODE)
    # dummy2 = TextNode("`This` is TEXTO ", TextType.TEXT)
    # dummy3 = TextNode("Isso é _itálico_", TextType.TEXT)
    # node = HTMLNode(props={
    #     "href": "http://www.google.com",
    #     "target": "_blank",
    # }, tag='h1', value="aaaaaa", children="a" )
    # html = node.props_to_html()

    new_nodes = split_nodes_delimiter([dummy], "`", text_type="CODE")
    # html2 = LeafNode("text", {"href":"www.example.com"}, "a")
    # print(html)
    # print(html2.to_html())
    # TestParentNode.test_to_html_with_multiple_children_with_multiple_grandchildren("")

main()