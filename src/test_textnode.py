import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_full(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://test.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://test.com")
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("Text 1", TextType.CODE)
        node2 = TextNode("Text2", TextType.IMAGE, 'http://theurl.com')
        self.assertNotEqual(node, node2)
    
    def test_text_to_html_node_text(self):
        node = TextNode("Text 1", TextType.TEXT).text_to_html_node().to_html()
        self.assertEqual(node, "Text 1")
    
    def test_text_to_html_node_bold(self):
        node = TextNode("Text 2", TextType.BOLD).text_to_html_node().to_html()
        self.assertEqual(node, "<b>Text 2</b>")
    
    def test_text_to_html_node_italic(self):
        node = TextNode("Text 3", TextType.ITALIC).text_to_html_node().to_html()
        self.assertEqual(node, "<i>Text 3</i>")

    def test_text_to_html_node_code(self):
        node = TextNode("Text 4", TextType.CODE).text_to_html_node().to_html()
        self.assertEqual(node, "<code>Text 4</code>")
    
    def test_text_to_html_node_link(self):
        node = TextNode("Text 5", TextType.LINK, "http://teste.com").text_to_html_node().to_html()
        self.assertEqual(node, "<a href=http://teste.com>Text 5</a>")

    def test_text_to_html_node_code(self):
        node = TextNode("Text 6", TextType.IMAGE, "http://teste2.com").text_to_html_node().to_html()
        self.assertEqual(node, "<img src=http://teste2.com alt=Text 6></img>")
    
    def test_text_to_html_node_exception(self):
        with self.assertRaises(Exception):
            TextNode("test", text_type="").text_to_html_node().to_html()

if __name__ == "__main__":
    unittest.main()