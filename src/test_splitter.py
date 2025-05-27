import unittest

from splitter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitter(unittest.TestCase):
    def test_text_node(self):
        node1 = TextNode("Dummy text", text_type=TextType.TEXT)
        new_node = split_nodes_delimiter([node1], "", TextType.TEXT)
        self.assertEqual(node1, new_node[0])

    
    def test_code_node(self):
        node = TextNode("`Code` text", text_type=TextType.CODE)
        new_node = split_nodes_delimiter([node], "`", TextType.CODE)
        expect = [
            TextNode("", TextType.TEXT, None), 
            TextNode("Code", TextType.CODE, None),
            TextNode(" text", TextType.TEXT, None)    
        ]
        self.assertListEqual(expect, new_node)

    def test_italic_node(self):
        node = TextNode("_italic_ text", text_type=TextType.ITALIC)
        new_node = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expect = [
            TextNode("", TextType.TEXT, None), 
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" text", TextType.TEXT, None)    
        ]
        self.assertListEqual(expect, new_node)

    def test_bold_node(self):
        node = TextNode("**Bold** text", text_type=TextType.BOLD)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        expect = [
            TextNode("", TextType.TEXT, None), 
            TextNode("Bold", TextType.BOLD, None),
            TextNode(" text", TextType.TEXT, None)    
        ]
        self.assertListEqual(expect, new_node)
    
    def test_multi_code(self):
        node = TextNode("`Code` text", text_type=TextType.CODE)
        node1 = TextNode("`Code2` text", text_type=TextType.CODE)
        new_node = split_nodes_delimiter([node, node1], "`", TextType.CODE)
        expect = [
            TextNode("", TextType.TEXT, None), 
            TextNode("Code", TextType.CODE, None),
            TextNode(" text", TextType.TEXT, None),
            TextNode("", TextType.TEXT, None), 
            TextNode("Code2", TextType.CODE, None),
            TextNode(" text", TextType.TEXT, None),       
        ]
        self.assertListEqual(expect, new_node)

    def test_code_twice(self):
        node = TextNode("`Code` and now `Code2`" ,text_type=TextType.CODE)
        new_node = split_nodes_delimiter([node], "`", TextType.CODE)
        expect = [
            TextNode("", TextType.TEXT, None),
            TextNode("Code", TextType.CODE, None), 
            TextNode(" and now ", TextType.TEXT, None), 
            TextNode("Code2", TextType.CODE, None), 
            TextNode("", TextType.TEXT, None)
        ]
        self.assertListEqual(new_node, expect)

    def test_no_closing_delimiter(self):
        node = TextNode("`Code` and now `Code2" ,text_type=TextType.CODE)
        with self.assertRaises(Exception):
            split_nodes_delimiter(node, "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()