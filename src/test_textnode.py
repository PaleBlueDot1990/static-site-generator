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


    def test_conversion_1(self):
        text_node = TextNode("This is a text node of type text", TextType.TEXT)
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node of type text")
        self.assertEqual(html_node.to_html(), "This is a text node of type text")
    

    def test_conversion_2(self):
        text_node = TextNode("This is a text node of type bold", TextType.BOLD)
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node of type bold")
        self.assertEqual(html_node.to_html(), "<b>This is a text node of type bold</b>")
    

    def test_conversion_3(self):
        text_node = TextNode("This is a text node of type italic", TextType.ITALIC)
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node of type italic")
        self.assertEqual(html_node.to_html(), "<i>This is a text node of type italic</i>")
    

    def test_conversion_4(self):
        text_node = TextNode("This is a text node of type code", TextType.CODE)
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node of type code")
        self.assertEqual(html_node.to_html(), "<code>This is a text node of type code</code>")


    def test_conversion_5(self):
        text_node = TextNode("This is a text node of type link", TextType.LINK, "https://google.com")
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a text node of type link")
        self.assertEqual(html_node.props, {"href" : text_node.url})
        self.assertEqual(
            html_node.to_html(), 
            "<a href=\"https://google.com\">This is a text node of type link</a>"
        )
    

    def test_conversion_6(self):
        text_node = TextNode("This is a text node of type image", TextType.IMAGE, "logo.png")
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src" : text_node.url, "alt" : text_node.text})
        self.assertEqual(
            html_node.to_html(), 
            "<img src=\"logo.png\" alt=\"This is a text node of type image\">"
        )
    
if __name__ == "__main__":
    unittest.main() 

