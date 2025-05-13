import unittest
from htmlnode import HTMLNode

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
    

if __name__ == "__main__":
    unittest.main() 






