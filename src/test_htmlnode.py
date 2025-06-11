import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("a", "teste1", None, {"href": "http://html.com"})
        node2 = LeafNode("a", "teste1", None, {"href": "http://html.com"})
        self.assertEqual(node1, node2)

    def test_to_html_exception(self):
        with self.assertRaises(ValueError):
            LeafNode("a", None, None, {"c": 1}).to_html()
        
    def test_to_html(self):
        node =  LeafNode("a", "teste1", None, {"href": "http://html.com"}).to_html()
        self.assertEqual(node, "<a href=http://html.com>teste1</a>")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!", None, {})
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], None)
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node], None)
        parent_node = ParentNode("div", [child_node], None)
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("b", "grandchild")
        child_node2 = LeafNode("a", "child 2", None, {"href": "http://teste.com"})
        child_node3 = LeafNode("", "no tag")
        parent_node = ParentNode("div", [child_node, child_node2, child_node3], None)
        parent_node.to_html()
        self.assertEqual(
            parent_node.to_html(), 
            "<div><b>grandchild</b><a href=http://teste.com>child 2</a>no tag</div>"
        )


    def test_to_html_with_multiple_children_with_one_grandchildren(self):
        grandchild_node_1 = LeafNode("b", "grandchild 1")
        grandchild_node_2 = LeafNode("a", "grandchild 2", None, {"href": "http://teste.com"})
        grandchild_node_3 = LeafNode("b", "grandchild 3")
        child_node = ParentNode("span", [grandchild_node_1, grandchild_node_2, grandchild_node_3], None)
        parent_node = ParentNode("div", [child_node], None)
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild 1</b><a href=http://teste.com>grandchild 2</a><b>grandchild 3</b></span></div>",
        )

    def test_to_html_with_multiple_children_with_multiple_grandchildren(self):
        child_1_grandchild_node_1 = LeafNode("b", "child_1_grandchild 1")
        child_1_grandchild_node_2 = LeafNode("a", "child_1_grandchild 2", None, {"href": "http://teste.com"})
        child_1_grandchild_node_3 = LeafNode("b", "child_1_grandchild 3")
        child_2_grandchild_node_1 = LeafNode("b", "child_2_grandchild 1")
        child_2_grandchild_node_2 = LeafNode("a", "child_2_grandchild 2", None, {"href": "http://teste2.com"})
        child_2_grandchild_node_3 = LeafNode("b", "child_2_grandchild 3")
        child_3_grandchild_node_1 = LeafNode("b", "child_3_grandchild 1")
        child_3_grandchild_node_2 = LeafNode("a", "child_3_grandchild 2", None, {"href": "http://teste3.com"})
        child_3_grandchild_node_3 = LeafNode("b", "child_3_grandchild 3", None, {"prop3": "prop3"})
        child_node_1 = ParentNode("span", [child_1_grandchild_node_1, child_1_grandchild_node_2, child_1_grandchild_node_3], None)
        child_node_2 = ParentNode("span", [child_2_grandchild_node_1, child_2_grandchild_node_2, child_2_grandchild_node_3], None)
        child_node_3 = ParentNode("span", [child_3_grandchild_node_1, child_3_grandchild_node_2, child_3_grandchild_node_3], None)
        parent_node = ParentNode("div", [child_node_1, child_node_2, child_node_3], None)
        self.assertEqual(parent_node.to_html(), "<div><span><b>child_1_grandchild 1</b><a href=http://teste.com>child_1_grandchild 2</a><b>child_1_grandchild 3</b></span><span><b>child_2_grandchild 1</b><a href=http://teste2.com>child_2_grandchild 2</a><b>child_2_grandchild 3</b></span><span><b>child_3_grandchild 1</b><a href=http://teste3.com>child_3_grandchild 2</a><b prop3=prop3>child_3_grandchild 3</b></span></div>")

if __name__ == "__main__":
    unittest.main()