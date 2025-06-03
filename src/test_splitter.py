import unittest

from splitter import *
from textnode import TextNode, TextType

class TestSplitter(unittest.TestCase):
    def test_text_node(self):
        node1 = TextNode("Dummy text", text_type=TextType.TEXT)
        new_node = split_nodes_delimiter([node1], "", TextType.TEXT)
        self.assertEqual(node1, new_node[0])

    
    def test_code_node(self):
        node = TextNode("`Code` text", text_type=TextType.TEXT)
        new_node = split_nodes_delimiter([node], "`", TextType.CODE)
        expect = [
            # TextNode("", TextType.TEXT, None), 
            TextNode("Code", TextType.CODE, None),
            TextNode(" text", TextType.TEXT, None)    
        ]
        self.assertListEqual(expect, new_node)

    def test_italic_node(self):
        node = TextNode("_italic_ text", text_type=TextType.TEXT)
        new_node = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expect = [
            # TextNode("", TextType.TEXT, None), 
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" text", TextType.TEXT, None)    
        ]
        self.assertListEqual(expect, new_node)

    def test_bold_node(self):
        node = TextNode("**Bold** text", text_type=TextType.TEXT)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        expect = [
            # TextNode("", TextType.TEXT, None), 
            TextNode("Bold", TextType.BOLD, None),
            TextNode(" text", TextType.TEXT, None)    
        ]
        self.assertListEqual(expect, new_node)
    
    def test_multi_code(self):
        node = TextNode("`Code` text", text_type=TextType.TEXT)
        node1 = TextNode("`Code2` text", text_type=TextType.TEXT)
        new_node = split_nodes_delimiter([node, node1], "`", TextType.CODE)
        expect = [
            # TextNode("", TextType.TEXT, None), 
            TextNode("Code", TextType.CODE, None),
            TextNode(" text", TextType.TEXT, None),
            # TextNode("", TextType.TEXT, None), 
            TextNode("Code2", TextType.CODE, None),
            TextNode(" text", TextType.TEXT, None),       
        ]
        self.assertListEqual(expect, new_node)

    def test_code_twice(self):
        node = TextNode("`Code` and now `Code2`" ,text_type=TextType.TEXT)
        new_node = split_nodes_delimiter([node], "`", TextType.CODE)
        expect = [
            # TextNode("", TextType.TEXT, None),
            TextNode("Code", TextType.CODE, None), 
            TextNode(" and now ", TextType.TEXT, None), 
            TextNode("Code2", TextType.CODE, None), 
            # TextNode("", TextType.TEXT, None)
        ]
        self.assertListEqual(new_node, expect)

    def test_no_closing_delimiter(self):
        node = TextNode("`Code` and now `Code2", text_type=TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_trailing(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and this is a trailing text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and this is a trailing text", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode("This is a paragraph with a [link](https://www.google.com)", TextType.TEXT)
        new_nodes = split_nodes_links([node])
        self.assertListEqual([
            TextNode("This is a paragraph with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.google.com"),
        ], new_nodes)

    
    def test_split_links_trailing(self):
        node = TextNode("This is a paragraph with a [link](https://www.google.com).", TextType.TEXT)
        new_nodes = split_nodes_links([node])
        self.assertListEqual([
            TextNode("This is a paragraph with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.google.com"),
            TextNode(".", TextType.TEXT)
        ], new_nodes)

    def test_text_to_textnode(self):
        node = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ], node)


if __name__ == "__main__":
    unittest.main()