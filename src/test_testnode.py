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

if __name__ == "__main__":
    unittest.main()