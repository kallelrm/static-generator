import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("a", "valor", "", {"teste 1": "1", "teste2": 2})
        node2 = HTMLNode("a", "valor", "", {"teste 1": "1", "teste2": 2})
        self.assertEqual(node1, node2)

    def test_ne(self):
        node1 = HTMLNode("b", "not empty")
        node2 = HTMLNode("b", "not empty2", "")
        self.assertNotEqual(node1, node2)
    
    def test_props_to_html(self):
        node = HTMLNode(props={'a':'a', 'b':'b', 'c':'c'}).props_to_html()
        self.assertEqual(node, "a=a b=b c=c")
    
if __name__ == "__main__":
    unittest.main()