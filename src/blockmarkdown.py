from enum import Enum
from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from inlinemarkdown import InlineMarkdown

class BlockType(Enum):
    PARAGRAPH = "Paragraph"
    HEADING = "Heading"
    CODE = "Code"
    QUOTE = "Quote"
    UNORDERED_LIST = "Unordered_List"
    ORDERED_LIST = "Ordered_List"

class BlockMarkDown():
    def markdown_to_blocks(self, markdown):
        blocks = markdown.split("\n\n")
        new_blocks = []

        for block in blocks:
            new_block = block.strip("\n")
            if len(new_block) != 0:            
                new_blocks.append(new_block)

        return new_blocks
    

    def block_to_block_type(self, block):
        if self.is_heading(block):
            return BlockType.HEADING
        elif self.is_code(block):
            return BlockType.CODE
        elif self.is_quote(block):
            return BlockType.QUOTE
        elif self.is_unordered_list(block):
            return BlockType.UNORDERED_LIST
        elif self.is_ordered_list(block):
            return BlockType.ORDERED_LIST
        else: 
            return BlockType.PARAGRAPH
    

    def is_heading(self, block):
        if block[0] != "#":
            return False
        idx = 0
        while idx < len(block) and block[idx] == "#":
            idx += 1
        return idx < len(block) and idx <= 6 and block[idx] == " "
        

    def is_code(self, block):
        return (
            len(block) >= 6 
            and block[:3] == "```" 
            and block[-3:] == "```"
        ) 


    def is_quote(self, block):
        return block[0] == '>'


    def is_unordered_list(self, block):
        list_items = block.split('\n')
        for list_item in list_items:
            if len(list_item) < 2 or list_item[0] != '-' or list_item[1] != ' ':
                return False
        return True


    def is_ordered_list(self, block):
        list_items = block.split('/n')
        list_idx = 1 
        for list_item in list_items:
            if len(list_item) < len(str(list_idx)) + 2:
                return False
            if list_item[:len(str(list_idx)) + 2] != str(list_idx) + ". ":
                return False 
            list_idx += 1
        return True 
    

    def markdown_to_html_node(self, markdown):
        blocks = self.markdown_to_blocks(markdown)
        root_node = ParentNode("div", [], None)

        for block in blocks:
            block_type = self.block_to_block_type(block)

            if block_type == BlockType.PARAGRAPH:
                p_node = self.get_paragraph_node(block)
                root_node.children.append(p_node)
            elif block_type == BlockType.HEADING:
                h_node = self.get_heading_node(block)
                root_node.children.append(h_node)
            elif block_type == BlockType.QUOTE:
                q_node = self.get_quote_node(block)
                root_node.children.append(q_node)
            elif block_type == BlockType.CODE:
                c_node = self.get_code_node(block)
                root_node.children.append(c_node)
            elif block_type == BlockType.UNORDERED_LIST:
                ul_node = self.get_unordered_list_node(block)
                root_node.children.append(ul_node)
            elif block_type == BlockType.ORDERED_LIST:
                ol_node = self.get_ordered_list_node(block)
                root_node.children.append(ol_node)
        
        return root_node
        
    
    def get_paragraph_node(self, block):
        parts = block.split("\n")
        block = " ".join(parts)

        text_nodes = InlineMarkdown().text_to_textnodes(block)
        if len(text_nodes) == 1:
            return LeafNode("div", block, None)

        p_node = ParentNode("p", [], None)
        for text_node in text_nodes:
            if text_node.text_type == TextType.TEXT:
                p_node.children.append(LeafNode(None, text_node.text, None))
            elif text_node.text_type == TextType.BOLD:
                p_node.children.append(LeafNode("b", text_node.text, None))
            elif text_node.text_type == TextType.CODE:
                p_node.children.append(LeafNode("code", text_node.text, None))
            elif text_node.text_type == TextType.ITALIC:
                p_node.children.append(LeafNode("i", text_node.text, None))
            elif text_node.text_type == TextType.IMAGE:
                p_node.children.append(LeafNode("img", "", {"src" : text_node.url, "alt" : text_node.text}))
            elif text_node.text_type == TextType.LINK:
                p_node.children.append(LeafNode("a", text_node.text, {"href" : text_node.url}))
        return p_node 
    

    def get_heading_node(self, block):
        h_tag, h_text = self.get_heading_details(block)
        parts = h_text.split("\n")
        h_text = " ".join(parts)

        text_nodes = InlineMarkdown().text_to_textnodes(h_text)
        if len(text_nodes) == 1:
            return LeafNode(h_tag, h_text, None)
        
        h_node = ParentNode(h_tag, [], None)
        for text_node in text_nodes:
            if text_node.text_type == TextType.TEXT:
                h_node.children.append(LeafNode(None, text_node.text, None))
            elif text_node.text_type == TextType.BOLD:
                h_node.children.append(LeafNode("b", text_node.text, None))
            elif text_node.text_type == TextType.CODE:
                h_node.children.append(LeafNode("code", text_node.text, None))
            elif text_node.text_type == TextType.ITALIC:
                h_node.children.append(LeafNode("i", text_node.text, None))
            elif text_node.text_type == TextType.IMAGE:
                h_node.children.append(LeafNode("img", "", {"src" : text_node.url, "alt" : text_node.text}))
            elif text_node.text_type == TextType.LINK:
                h_node.children.append(LeafNode("a", text_node.text, {"href" : text_node.url}))
        return h_node
    

    def get_quote_node(self, block):
        q_tag, q_text = "blockquote", block[1:]
        parts = q_text.split("\n")
        q_text = " ".join(parts)

        text_nodes = InlineMarkdown().text_to_textnodes(q_text)
        if len(text_nodes) == 1:
            return LeafNode(q_tag, q_text, None)
        
        q_node = ParentNode(q_tag, [], None)
        for text_node in text_nodes:
            if text_node.text_type == TextType.TEXT:
                q_node.children.append(LeafNode(None, text_node.text, None))
            elif text_node.text_type == TextType.BOLD:
                q_node.children.append(LeafNode("b", text_node.text, None))
            elif text_node.text_type == TextType.CODE:
                q_node.children.append(LeafNode("code", text_node.text, None))
            elif text_node.text_type == TextType.ITALIC:
                q_node.children.append(LeafNode("i", text_node.text, None))
            elif text_node.text_type == TextType.IMAGE:
                q_node.children.append(LeafNode("img", "", {"src" : text_node.url, "alt" : text_node.text}))
            elif text_node.text_type == TextType.LINK:
                q_node.children.append(LeafNode("a", text_node.text, {"href" : text_node.url}))
        return q_node
    

    def get_unordered_list_node(self, block):
        ul_node = ParentNode("ul", [], None)
        list_items = block.split("\n")

        for list_item in list_items:
            item_text = list_item[2:]
            text_nodes = InlineMarkdown().text_to_textnodes(item_text)
            if len(text_nodes) == 1:
                ul_node.children.append(LeafNode("li", item_text, None))
            
            li_node = ParentNode("li", [], None)
            for text_node in text_nodes:
                if text_node.text_type == TextType.TEXT:
                    li_node.children.append(LeafNode(None, text_node.text, None))
                elif text_node.text_type == TextType.BOLD:
                    li_node.children.append(LeafNode("b", text_node.text, None))
                elif text_node.text_type == TextType.CODE:
                    li_node.children.append(LeafNode("code", text_node.text, None))
                elif text_node.text_type == TextType.ITALIC:
                    li_node.children.append(LeafNode("i", text_node.text, None))
                elif text_node.text_type == TextType.IMAGE:
                    li_node.children.append(LeafNode("img", "", {"src" : text_node.url, "alt" : text_node.text}))
                elif text_node.text_type == TextType.LINK:
                    li_node.children.append(LeafNode("a", text_node.text, {"href" : text_node.url}))
            ul_node.children.append(li_node)
        
        return ul_node
    

    def get_ordered_list_node(self, block):
        ol_node = ParentNode("ol", [], None)
        list_items = block.split("\n")

        for list_item in list_items:
            item_text = self.get_ordered_item_text(list_item)
            text_nodes = InlineMarkdown().text_to_textnodes(item_text)
            if len(text_nodes) == 1:
                ol_node.children.append(LeafNode("li", item_text, None))
            
            li_node = ParentNode("li", [], None)
            for text_node in text_nodes:
                if text_node.text_type == TextType.TEXT:
                    li_node.children.append(LeafNode(None, text_node.text, None))
                elif text_node.text_type == TextType.BOLD:
                    li_node.children.append(LeafNode("b", text_node.text, None))
                elif text_node.text_type == TextType.CODE:
                    li_node.children.append(LeafNode("code", text_node.text, None))
                elif text_node.text_type == TextType.ITALIC:
                    li_node.children.append(LeafNode("i", text_node.text, None))
                elif text_node.text_type == TextType.IMAGE:
                    li_node.children.append(LeafNode("img", "", {"src" : text_node.url, "alt" : text_node.text}))
                elif text_node.text_type == TextType.LINK:
                    li_node.children.append(LeafNode("a", text_node.text, {"href" : text_node.url}))
            ol_node.children.append(li_node)
        
        return ol_node
    

    def get_code_node(self, block):
        code_text = block[3:-3]
        code_node = LeafNode("code", code_text, None)
        pre_node = ParentNode("pre", [code_node], None)
        return pre_node


    def get_heading_details(self, block):
        idx = 0
        for c in block:
            if c != "#":
                break
            idx += 1
        
        h_tag = f"h{idx}"
        h_text = block[idx+1:]
        return h_tag, h_text
        

    def get_ordered_item_text(self, block):
        text = block.split('.', 1)[1].strip()
        return text 
        

    






    


