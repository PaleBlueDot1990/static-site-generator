import re 
from textnode import TextNode, TextType

class InlineMarkdownNodeSplitter():
    def split_nodes_delimiter(self, old_nodes, delimiter, text_type):
        new_nodes = []

        for old_node in old_nodes:
            if old_node.text_type != TextType.TEXT:
                new_nodes.append(old_node)
                continue

            parts = old_node.text.split(delimiter)
            for idx, part in enumerate(parts):
                if idx % 2 == 0:
                    if len(part) > 0:
                        new_nodes.append(TextNode(part, old_node.text_type))
                else:
                    new_nodes.append(TextNode(part, text_type))
        
        return new_nodes
    

    def extract_markdown_images(self, text):
        matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
        return matches


    def extract_markdown_links(self, text):
        matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
        return matches 


    def split_nodes_link(self, old_nodes):
        new_nodes = []

        for old_node in old_nodes:
            if old_node.text_type != TextType.TEXT:
                new_nodes.append(old_node)
                continue 

            remaining_text = old_node.text 
            links = self.extract_markdown_links(remaining_text)

            if len(links) == 0:
                new_nodes.append(old_node)
                continue 

            for link_text, link_url in links:
                delimiter = f"[{link_text}]({link_url})"
                parts = remaining_text.split(delimiter, 1)
                before_link = parts[0]
                after_link = parts[1]

                if len(before_link) > 0:
                    new_nodes.append(TextNode(before_link, TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                remaining_text = after_link

            if len(remaining_text) > 0:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT)) 

        return new_nodes  

    
    def split_nodes_image(self, old_nodes):
        new_nodes = []

        for old_node in old_nodes:
            if old_node.text_type != TextType.TEXT:
                new_nodes.append(old_node)
                continue 

            remaining_text = old_node.text 
            images = self.extract_markdown_images(remaining_text)

            if len(images) == 0:
                new_nodes.append(old_node)
                continue 

            for image_text, image_url in images:
                delimiter = f"![{image_text}]({image_url})"
                parts = remaining_text.split(delimiter, 1)
                before_link = parts[0]
                after_link = parts[1]

                if len(before_link) > 0:
                    new_nodes.append(TextNode(before_link, TextType.TEXT))
                new_nodes.append(TextNode(image_text, TextType.IMAGE, image_url))
                remaining_text = after_link

            if len(remaining_text) > 0:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))  

        return new_nodes  

    
    def text_to_textnodes(self, markdown_text):
        node = TextNode(markdown_text, TextType.TEXT)
        node_list = [node]

        node_list = self.split_nodes_delimiter(node_list, "**", TextType.BOLD)
        node_list = self.split_nodes_delimiter(node_list, "`", TextType.CODE)
        node_list = self.split_nodes_delimiter(node_list, "_", TextType.ITALIC)
        node_list = self.split_nodes_link(node_list)
        node_list = self.split_nodes_image(node_list)

        return node_list
