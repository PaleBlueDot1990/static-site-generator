import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)
    
    def test_eq2(self):
        node1 = TextNode("This is a text node", TextType.LINK, "Dummy link 1")
        node2 = TextNode("This is a text node", TextType.LINK, "Dummy link 1")
        self.assertEqual(node1, node2) 
    
    def test_not_eq1(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    
    def test_not_eq2(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_not_eq3(self):
        node1 = TextNode("This is a text node", TextType.LINK, "Dummy link 1")
        node2 = TextNode("This is a text node", TextType.LINK, "Dummy link 2")
        self.assertNotEqual(node1, node2) 

    def test_not_eq4(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None) 
    
if __name__ == "__main__":
    unittest.main() 

