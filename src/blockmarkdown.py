from enum import Enum

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
        
