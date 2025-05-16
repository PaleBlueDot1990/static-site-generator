import unittest
from textnode import TextNode, TextType
from inlinemarkdown import InlineMarkdown


class TestSplitNodesByDelimiter(unittest.TestCase):
    def test_sinlge_delimiter_1(self):
        node = TextNode("hello my name is bhuvnesh", TextType.TEXT)
        old_nodes = [node]
        new_nodes = InlineMarkdown().split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        self.assertListEqual(new_nodes, [
            TextNode("hello my name is bhuvnesh", TextType.TEXT)
        ])


    def test_single_delimiter_2(self):
        node = TextNode("`hello` my name is bhuvnesh", TextType.TEXT)
        old_nodes = [node]
        new_nodes = InlineMarkdown().split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        self.assertListEqual(new_nodes, [
            TextNode("hello", TextType.CODE),
            TextNode(" my name is bhuvnesh", TextType.TEXT)
        ])
        
    
    def test_single_delimiter_3(self):
        node = TextNode("hello my name is `bhuvnesh`", TextType.TEXT)
        old_nodes = [node]
        new_nodes = InlineMarkdown().split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        self.assertListEqual(new_nodes, [
            TextNode("hello my name is ", TextType.TEXT),
            TextNode("bhuvnesh", TextType.CODE)
        ])
    

    def test_single_delimiter_3(self):
        node = TextNode("hello my `name` is bhuvnesh", TextType.TEXT)
        old_nodes = [node]
        new_nodes = InlineMarkdown().split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        self.assertListEqual(new_nodes, [
            TextNode("hello my ", TextType.TEXT),
            TextNode("name", TextType.CODE),
            TextNode(" is bhuvnesh", TextType.TEXT)
        ])
    

    def test_single_delimiter_4(self):
        node = TextNode("`hello` my name is `bhuvnesh`", TextType.TEXT)
        old_nodes = [node]
        new_nodes = InlineMarkdown().split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        self.assertListEqual(new_nodes, [
            TextNode("hello", TextType.CODE),
            TextNode(" my name is ", TextType.TEXT),
            TextNode("bhuvnesh", TextType.CODE)
        ])
    

    def test_single_delimiter_5(self):
        node = TextNode("`hello` my `name` is `bhuvnesh`", TextType.TEXT)
        old_nodes = [node]
        new_nodes = InlineMarkdown().split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        self.assertListEqual(new_nodes, [
            TextNode("hello", TextType.CODE),
            TextNode(" my ", TextType.TEXT),
            TextNode("name", TextType.CODE),
            TextNode(" is ", TextType.TEXT),
            TextNode("bhuvnesh", TextType.CODE)
        ])
    

    def test_single_delimiter_6(self):
        node = TextNode("`hello` `my` `name` `is` `bhuvnesh`", TextType.TEXT)
        old_nodes = [node]
        new_nodes = InlineMarkdown().split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        self.assertListEqual(new_nodes, [
            TextNode("hello", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("my", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("name", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("is", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("bhuvnesh", TextType.CODE)
        ])


    def test_single_delimiter_7(self):
        node = TextNode("hello my name is `bhuv``nesh`", TextType.TEXT)
        old_nodes = [node]
        new_nodes = InlineMarkdown().split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        self.assertListEqual(new_nodes, [
            TextNode("hello my name is ", TextType.TEXT),
            TextNode("bhuv", TextType.CODE),
            TextNode("nesh", TextType.CODE)
        ])


    def test_multiple_delimiters_1(self):
        node = TextNode("**hello** `my name is` _bhuvnesh_", TextType.TEXT)
        new_nodes = [node]

        utils = InlineMarkdown()
        new_nodes = utils.split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        new_nodes = utils.split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        new_nodes = utils.split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)

        self.assertListEqual(new_nodes, [
            TextNode("hello", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("my name is", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("bhuvnesh", TextType.ITALIC)
        ])
    

    def test_multiple_delimiters_2(self):
        node = TextNode("**hello** **my** name _is_ _bhuvnesh_", TextType.TEXT)
        new_nodes = [node]

        utils = InlineMarkdown()
        new_nodes = utils.split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        new_nodes = utils.split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        new_nodes = utils.split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)

        self.assertListEqual(new_nodes, [
            TextNode("hello", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("my", TextType.BOLD),
            TextNode(" name ", TextType.TEXT),
            TextNode("is", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("bhuvnesh", TextType.ITALIC)
        ])


class TestImageLinkExtraction(unittest.TestCase):
    def test_single_image_extraction_1(self):
        text = "![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = InlineMarkdown().extract_markdown_images(text)

        self.assertListEqual(matches, [
            ("image", "https://i.imgur.com/zjjcJKZ.png")
        ])
    
    
    def test_single_image_extraction_2(self):
        text = "Some text ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = InlineMarkdown().extract_markdown_images(text)

        self.assertListEqual(matches, [
            ("image", "https://i.imgur.com/zjjcJKZ.png")
        ])
    

    def test_single_image_extraction_3(self):
        text = "![image](https://i.imgur.com/zjjcJKZ.png) Some text"
        matches = InlineMarkdown().extract_markdown_images(text)

        self.assertListEqual(matches, [
            ("image", "https://i.imgur.com/zjjcJKZ.png")
        ])
    

    def test_multiple_image_extraction_1(self):
        text = "![image1](https://i.imgur.com/zjjcJKZ.png) ![image2](https://i.imgur.com/xshaGFR.png)"
        matches = InlineMarkdown().extract_markdown_images(text)

        self.assertListEqual(matches, [
            ("image1", "https://i.imgur.com/zjjcJKZ.png"),
            ("image2", "https://i.imgur.com/xshaGFR.png")
        ])
    

    def test_multiple_image_extraction_2(self):
        text = "text1 ![image1](https://i.imgur.com/zjjcJKZ.png) text2 ![image2](https://i.imgur.com/xshaGFR.png) text3"
        matches = InlineMarkdown().extract_markdown_images(text)

        self.assertListEqual(matches, [
            ("image1", "https://i.imgur.com/zjjcJKZ.png"),
            ("image2", "https://i.imgur.com/xshaGFR.png")
        ])


    def test_single_link_extraction_1(self):
        text = "[to boot dev](https://www.boot.dev)"
        matches = InlineMarkdown().extract_markdown_links(text)

        self.assertListEqual(matches, [
            ("to boot dev", "https://www.boot.dev")
        ])
    

    def test_single_link_extraction_2(self):
        text = "Some text [to boot dev](https://www.boot.dev)"
        matches = InlineMarkdown().extract_markdown_links(text)

        self.assertListEqual(matches, [
            ("to boot dev", "https://www.boot.dev")
        ])
    

    def test_single_link_extraction_3(self):
        text = "[to boot dev](https://www.boot.dev) some text"
        matches = InlineMarkdown().extract_markdown_links(text)

        self.assertListEqual(matches, [
            ("to boot dev", "https://www.boot.dev")
        ])
    

    def test_multiple_link_extraction_1(self):
        text = "[to google](https://www.google.com/) [to youtube](https://www.youtube.com/)"
        matches = InlineMarkdown().extract_markdown_links(text)

        self.assertListEqual(matches, [
            ("to google", "https://www.google.com/"),
            ("to youtube", "https://www.youtube.com/")
        ])
    

    def test_multiple_link_extraction_2(self):
        text = "text1 [to google](https://www.google.com/) text2 [to youtube](https://www.youtube.com/) text3"
        matches = InlineMarkdown().extract_markdown_links(text)

        self.assertListEqual(matches, [
            ("to google", "https://www.google.com/"),
            ("to youtube", "https://www.youtube.com/")
        ])


class TestSplitNodesByImageLink(unittest.TestCase):
    def test_single_link_split_1(self):
        node = TextNode("[to google](https://www.google.com/)", TextType.TEXT)
        new_nodes = InlineMarkdown().split_nodes_link([node])

        self.assertEqual([
            TextNode("to google", TextType.LINK, "https://www.google.com/")
        ], new_nodes)
    

    def test_single_link_split_2(self):
        node = TextNode("text [to google](https://www.google.com/)", TextType.TEXT)
        new_nodes = InlineMarkdown().split_nodes_link([node])

        self.assertEqual([
            TextNode("text ", TextType.TEXT),
            TextNode("to google", TextType.LINK, "https://www.google.com/")
        ], new_nodes)
    

    def test_single_link_split_3(self):
        node = TextNode("[to google](https://www.google.com/) text", TextType.TEXT)
        new_nodes = InlineMarkdown().split_nodes_link([node])

        self.assertEqual([
            TextNode("to google", TextType.LINK, "https://www.google.com/"),
            TextNode(" text", TextType.TEXT)
        ], new_nodes)
    
    
    def test_multiple_links_split_1(self):
        node = TextNode("[to google](https://www.google.com/) [to youtube](https://www.youtube.com/)", TextType.TEXT)
        new_nodes = InlineMarkdown().split_nodes_link([node])

        self.assertEqual([
            TextNode("to google", TextType.LINK, "https://www.google.com/"),
            TextNode(" ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/")
        ], new_nodes)
    

    def test_multiple_links_split_2(self):
        node = TextNode("text1 [to google](https://www.google.com/) text2 [to youtube](https://www.youtube.com/) text3", TextType.TEXT)
        new_nodes = InlineMarkdown().split_nodes_link([node])

        self.assertEqual([
            TextNode("text1 ", TextType.TEXT),
            TextNode("to google", TextType.LINK, "https://www.google.com/"),
            TextNode(" text2 ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/"),
            TextNode(" text3", TextType.TEXT)
        ], new_nodes)

    
    def test_single_image_split_1(self):
        node = TextNode("![image](https://i.imgur.com/xhsAJU.png)", TextType.TEXT)
        new_nodes = InlineMarkdown().split_nodes_image([node])

        self.assertEqual([
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/xhsAJU.png")
        ], new_nodes)
    

    def test_single_image_split_2(self):
        node = TextNode("text ![image](https://i.imgur.com/xhsAJU.png)", TextType.TEXT)
        new_nodes = InlineMarkdown().split_nodes_image([node])

        self.assertEqual([
            TextNode("text ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/xhsAJU.png")
        ], new_nodes)
    

    def test_single_image_split_3(self):
        node = TextNode("![image](https://i.imgur.com/xhsAJU.png) text", TextType.TEXT)
        new_nodes = InlineMarkdown().split_nodes_image([node])

        self.assertEqual([
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/xhsAJU.png"),
            TextNode(" text", TextType.TEXT)
        ], new_nodes)
    

    def test_multiple_image_split_1(self):
        node = TextNode("![image1](https://i.imgur.com/xhsAJU.png) ![image2](https://i.imgur.com/kshNME.png)", TextType.TEXT)
        new_nodes = InlineMarkdown().split_nodes_image([node])

        self.assertEqual([
            TextNode("image1", TextType.IMAGE, "https://i.imgur.com/xhsAJU.png"),
            TextNode(" ", TextType.TEXT),
            TextNode("image2", TextType.IMAGE, "https://i.imgur.com/kshNME.png")
        ], new_nodes)
    

    def test_multiple_image_split_2(self):
        node = TextNode("text1 ![image1](https://i.imgur.com/xhsAJU.png) text2 ![image2](https://i.imgur.com/kshNME.png) text3", TextType.TEXT)
        new_nodes = InlineMarkdown().split_nodes_image([node])

        self.assertEqual([
            TextNode("text1 ", TextType.TEXT),
            TextNode("image1", TextType.IMAGE, "https://i.imgur.com/xhsAJU.png"),
            TextNode(" text2 ", TextType.TEXT),
            TextNode("image2", TextType.IMAGE, "https://i.imgur.com/kshNME.png"),
            TextNode(" text3", TextType.TEXT)
        ], new_nodes)
    

class TestSplitNodes(unittest.TestCase):
    def test_nodes_split_1(self):
        markdown_text = "This is **text** with an _italic_ word and a `code block` and a ![sample image](https://i.imgur.com/fJRm4Vk.jpeg) and a [sample link](https://www.google.com)"
        new_nodes = InlineMarkdown().text_to_textnodes(markdown_text)

        self.assertListEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and a ", TextType.TEXT),
            TextNode("sample image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("sample link", TextType.LINK, "https://www.google.com")
        ])
    

    def test_nodes_split_2(self):
        markdown_text = "This is _text_ with a `code block` word and a **bold** word and a [sample link](https://www.google.com) and a ![sample image](https://i.imgur.com/fJRm4Vk.jpeg)"
        new_nodes = InlineMarkdown().text_to_textnodes(markdown_text)

        self.assertListEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.ITALIC),
            TextNode(" with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("sample link", TextType.LINK, "https://www.google.com"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("sample image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
        ])
    

    def test_nodes_split_3(self):
        markdown_text = "This is a text without any style"
        new_nodes = InlineMarkdown().text_to_textnodes(markdown_text)

        self.assertListEqual(new_nodes, [
            TextNode("This is a text without any style", TextType.TEXT)
        ])
    

    def test_nodes_split_4(self):
        markdown_text = "**Bold**`Code1`_Italic_`Code2`"
        new_nodes = InlineMarkdown().text_to_textnodes(markdown_text)

        self.assertListEqual(new_nodes, [
            TextNode("Bold", TextType.BOLD),
            TextNode("Code1", TextType.CODE),
            TextNode("Italic", TextType.ITALIC),
            TextNode("Code2", TextType.CODE)
        ])
    

    def test_nodes_split_5(self):
        markdown_text = "`Code1`**Bold1**_Italic1_![img1](iurl1)[link1](lurl1)`Code2`[link2](lurl2)![img2](iurl2)**Bold2**"
        new_nodes = InlineMarkdown().text_to_textnodes(markdown_text)

        self.assertListEqual(new_nodes, [
            TextNode("Code1", TextType.CODE),
            TextNode("Bold1", TextType.BOLD),
            TextNode("Italic1", TextType.ITALIC),
            TextNode("img1", TextType.IMAGE, "iurl1"),
            TextNode("link1", TextType.LINK, "lurl1"),
            TextNode("Code2", TextType.CODE),
            TextNode("link2", TextType.LINK, "lurl2"),
            TextNode("img2", TextType.IMAGE, "iurl2"),
            TextNode("Bold2", TextType.BOLD)
        ])
    







    

    




    


