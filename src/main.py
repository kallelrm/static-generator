from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
from splitter import split_nodes_delimiter
from test_htmlnode import TestParentNode
from extractor import extract_markdown_images, extract_markdown_links
def main():
    dummy = TextNode("`This`` is CODE TEXTO ", TextType.TEXT)
    # dummy2 = TextNode("`This` is TEXTO ", TextType.TEXT)
    # dummy3 = TextNode("Isso é _itálico_", TextType.TEXT)
    # node = HTMLNode(props={
    #     "href": "http://www.google.com",
    #     "target": "_blank",
    # }, tag='h1', value="aaaaaa", children="a" )
    # html = node.props_to_html()

    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

    # text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

    # print(extract_markdown_images(text))
    # print(extract_markdown_links(text2))
    new_nodes = split_nodes_delimiter([dummy], "`", TextType.CODE)
    print(new_nodes)
    # html2 = LeafNode("text", {"href":"www.example.com"}, "a")
    # print(html)
    # print(html2.to_html())
    # TestParentNode.test_to_html_with_multiple_children_with_multiple_grandchildren("")

main()