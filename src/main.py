from textnode import TextType, TextNode
from htmlnode import HTMLNode


def main():
    bold_text_node = TextNode("Bold Node", TextType.BOLD)
    code_text_node = TextNode("Code Node", TextType.CODE)
    link_text_node = TextNode("Link Node", TextType.LINK, "Dummy Link")
    img_text_node = TextNode("Image Node", TextType.IMAGE, "Dummy Url")

    print(bold_text_node)
    print(code_text_node)
    print(link_text_node)
    print(img_text_node)

    para_html_node = HTMLNode(tag="p", value="This is a paragraph.")
    h1_html_node = HTMLNode(tag="h1", value="Welcome to My Website")
    anchor_html_node = HTMLNode(tag="a", value="Click here", props={"href": "https://example.com", "target": "_blank"})
    img_html_node = HTMLNode(tag="img", props={"src": "logo.png", "alt": "Site Logo"})

    print(para_html_node)
    print(h1_html_node)
    print(anchor_html_node)
    print(img_html_node)


if __name__ == "__main__":
    main()