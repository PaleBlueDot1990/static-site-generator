import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHtmlNode(unittest.TestCase):
    def test_para_node(self):
        node = HTMLNode(tag="p", value="This is a paragraph.")
        self.assertEqual(node.props, {})
        self.assertEqual(node.children, [])
    
    
    def test_img_node(self):
        node = HTMLNode(tag="img", props={"src": "logo.png", "alt": "Site Logo"})
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, [])
    

    def test_anchor_node(self):
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.children, [])


class TestLeafNode(unittest.TestCase):
    def test_para_leaf_node(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(
            node.to_html(), 
            "<p>Hello, world!</p>"
        )

    
    def test_anchor_leaf_node(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), 
            "<a href=\"https://www.google.com\">Click me!</a>"
        )

    
    def test_image_leaf_node(self):
        node = LeafNode("img", "", props={"src": "logo.png", "alt": "Site Logo"})
        self.assertEqual(
            node.to_html(), 
            "<img src=\"logo.png\" alt=\"Site Logo\">"
        )



class TestParentNode(unittest.TestCase):
    def test_parent_node_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span>child</span></div>"
        )
    

    def test_parent_node_with_children(self):
        child_node_1 = LeafNode("span", "child1")
        child_node_2 = LeafNode("b", "child2")
        parent_node = ParentNode("div", [child_node_1, child_node_2])
        self.assertEqual(
            parent_node.to_html(), 
            "<div><span>child1</span><b>child2</b></div>"
        )


    def test_parent_node_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    

    def test_parent_node_with_parent_node(self):
        child_node_1 = LeafNode("b", "Child_1")

        grand_child_1 = LeafNode("a", "Grand_Child_1", {"href": "https://www.google.com"})
        grand_child_2 = LeafNode("img", "", props={"src": "logo.png", "alt": "Site_Logo"})
        grand_child_3 = LeafNode("h5", "Grand_Child_3")
        child_node_2 = ParentNode("p", [grand_child_1, grand_child_2, grand_child_3])

        node = ParentNode("p", [child_node_1, child_node_2])
        self.assertEqual(
            node.to_html(),
            "<p><b>Child_1</b><p><a href=\"https://www.google.com\">Grand_Child_1</a><img src=\"logo.png\" alt=\"Site_Logo\"><h5>Grand_Child_3</h5></p></p>"
        )
        
    

if __name__ == "__main__":
    unittest.main() 






