import unittest
from blockmarkdown import BlockMarkDown, BlockType

class TestBlockMarkDown(unittest.TestCase):
    def test_markdown_to_blocks_1(self):
        md = """
This is a **bold** paragraph


This is another _paragraph_ with `code`
This is the same paragraph on a new line



- Unordered List Item 1
- Unordered List Item 2
- Unordered List Item 3


"""
        blocks = BlockMarkDown().markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a **bold** paragraph",
                "This is another _paragraph_ with `code`\nThis is the same paragraph on a new line",
                "- Unordered List Item 1\n- Unordered List Item 2\n- Unordered List Item 3",
            ],
        )
    

    def test_markdown_to_blocks_2(self):
        md = """



# This is a heading

## This is another heading



This is a paragraph
This is same paragraph

This is another paragraph

- Unordered List Item 1
- Unordered List Item 2
- Unordered List Item 3


1. Ordered List Item 1
2. Ordered List Item 2
3. Ordered List Item 3


"""
        blocks = BlockMarkDown().markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "## This is another heading",
                "This is a paragraph\nThis is same paragraph",
                "This is another paragraph",
                "- Unordered List Item 1\n- Unordered List Item 2\n- Unordered List Item 3",
                "1. Ordered List Item 1\n2. Ordered List Item 2\n3. Ordered List Item 3"
            ]
        )


    def test_markdown_to_blocks_3(self):
        md = """
# This is a heading

This is a paragraph
with a second line
and with a third line

> This is a quote

```
This is a code block
with some code snippets
```



```
This is second code block
with some code snippets
```


> This is a second quote

1. First Ordered List Item 1
2. First Ordered List Item 2
3. First Ordered List Item 3




1. Second Ordered List Item 1
2. Second Ordered List Item 2
3. Second Ordered List Item 3
"""
        blocks = BlockMarkDown().markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph\nwith a second line\nand with a third line",
                "> This is a quote",
                "```\nThis is a code block\nwith some code snippets\n```",
                "```\nThis is second code block\nwith some code snippets\n```",
                "> This is a second quote",
                "1. First Ordered List Item 1\n2. First Ordered List Item 2\n3. First Ordered List Item 3",
                "1. Second Ordered List Item 1\n2. Second Ordered List Item 2\n3. Second Ordered List Item 3"
            ]
        )
    

    def test_block_to_block_type_1(self):
        h1 = "# Heading 1"
        h2 = "## Heading 2"
        h3 = "### Heading 3"
        h4 = "#### Heading 4"
        h5 = "##### Heading 5"
        h6 = "###### Heading 6"
        
        type1 = BlockMarkDown().block_to_block_type(h1)
        type2 = BlockMarkDown().block_to_block_type(h2)
        type3 = BlockMarkDown().block_to_block_type(h3)
        type4 = BlockMarkDown().block_to_block_type(h4)
        type5 = BlockMarkDown().block_to_block_type(h5)
        type6 = BlockMarkDown().block_to_block_type(h6)

        self.assertEqual(type1, BlockType.HEADING)
        self.assertEqual(type2, BlockType.HEADING)
        self.assertEqual(type3, BlockType.HEADING)
        self.assertEqual(type4, BlockType.HEADING)
        self.assertEqual(type5, BlockType.HEADING)
        self.assertEqual(type6, BlockType.HEADING)
    

    def test_block_to_block_type_2(self):
        h1 = "# "
        h2 = "## "
        h3 = "### "
        h4 = "#### "
        h5 = "##### "
        h6 = "###### "
        
        type1 = BlockMarkDown().block_to_block_type(h1)
        type2 = BlockMarkDown().block_to_block_type(h2)
        type3 = BlockMarkDown().block_to_block_type(h3)
        type4 = BlockMarkDown().block_to_block_type(h4)
        type5 = BlockMarkDown().block_to_block_type(h5)
        type6 = BlockMarkDown().block_to_block_type(h6)

        self.assertEqual(type1, BlockType.HEADING)
        self.assertEqual(type2, BlockType.HEADING)
        self.assertEqual(type3, BlockType.HEADING)
        self.assertEqual(type4, BlockType.HEADING)
        self.assertEqual(type5, BlockType.HEADING)
        self.assertEqual(type6, BlockType.HEADING)
    

    def test_block_to_block_type_3(self):
        h1 = "#Heading 1"
        h2 = "##Heading 2"
        h3 = "###Heading 3"
        h4 = "####Heading 4"
        h5 = "#####Heading 5"
        h6 = "######Heading 6"
        
        type1 = BlockMarkDown().block_to_block_type(h1)
        type2 = BlockMarkDown().block_to_block_type(h2)
        type3 = BlockMarkDown().block_to_block_type(h3)
        type4 = BlockMarkDown().block_to_block_type(h4)
        type5 = BlockMarkDown().block_to_block_type(h5)
        type6 = BlockMarkDown().block_to_block_type(h6)

        self.assertNotEqual(type1, BlockType.HEADING)
        self.assertNotEqual(type2, BlockType.HEADING)
        self.assertNotEqual(type3, BlockType.HEADING)
        self.assertNotEqual(type4, BlockType.HEADING)
        self.assertNotEqual(type5, BlockType.HEADING)
        self.assertNotEqual(type6, BlockType.HEADING)
    

    def test_block_to_block_type_4(self):
        h1 = "#"
        h2 = "##"
        h3 = "###"
        h4 = "####"
        h5 = "#####"
        h6 = "######"
        
        type1 = BlockMarkDown().block_to_block_type(h1)
        type2 = BlockMarkDown().block_to_block_type(h2)
        type3 = BlockMarkDown().block_to_block_type(h3)
        type4 = BlockMarkDown().block_to_block_type(h4)
        type5 = BlockMarkDown().block_to_block_type(h5)
        type6 = BlockMarkDown().block_to_block_type(h6)

        self.assertNotEqual(type1, BlockType.HEADING)
        self.assertNotEqual(type2, BlockType.HEADING)
        self.assertNotEqual(type3, BlockType.HEADING)
        self.assertNotEqual(type4, BlockType.HEADING)
        self.assertNotEqual(type5, BlockType.HEADING)
        self.assertNotEqual(type6, BlockType.HEADING)
    

    def test_block_to_block_type_5(self):
        h1 = " "
        h2 = " #"
        h3 = "Heading"
        h4 = " Heading"
        h5 = "#######"
        h6 = "####### "
        h7 = "#######  Heading"
        
        type1 = BlockMarkDown().block_to_block_type(h1)
        type2 = BlockMarkDown().block_to_block_type(h2)
        type3 = BlockMarkDown().block_to_block_type(h3)
        type4 = BlockMarkDown().block_to_block_type(h4)
        type5 = BlockMarkDown().block_to_block_type(h5)
        type6 = BlockMarkDown().block_to_block_type(h6)
        type7 = BlockMarkDown().block_to_block_type(h7)

        self.assertNotEqual(type1, BlockType.HEADING)
        self.assertNotEqual(type2, BlockType.HEADING)
        self.assertNotEqual(type3, BlockType.HEADING)
        self.assertNotEqual(type4, BlockType.HEADING)
        self.assertNotEqual(type5, BlockType.HEADING)
        self.assertNotEqual(type6, BlockType.HEADING)
        self.assertNotEqual(type7, BlockType.HEADING)


    def test_block_to_block_type_6(self):
        code1 = "```"
        code2 = "````"
        code3 = "`````"
        code4 = "``Code``"
        code5 = "```Code``"
        code6 = "``Code```"
        code7 = "```Code"
        code8 = "Code```"
        code9 = " ```Code```"
        code10 = "```Code``` "
        code11 = " ```Code``` "

        type1 = BlockMarkDown().block_to_block_type(code1)
        type2 = BlockMarkDown().block_to_block_type(code2)
        type3 = BlockMarkDown().block_to_block_type(code3)
        type4 = BlockMarkDown().block_to_block_type(code4)
        type5 = BlockMarkDown().block_to_block_type(code5)
        type6 = BlockMarkDown().block_to_block_type(code6)
        type7 = BlockMarkDown().block_to_block_type(code7)
        type8 = BlockMarkDown().block_to_block_type(code8)
        type9 = BlockMarkDown().block_to_block_type(code9)
        type10 = BlockMarkDown().block_to_block_type(code10)
        type11 = BlockMarkDown().block_to_block_type(code11)


        self.assertNotEqual(type1, BlockType.CODE)
        self.assertNotEqual(type2, BlockType.CODE)
        self.assertNotEqual(type3, BlockType.CODE)
        self.assertNotEqual(type4, BlockType.CODE)
        self.assertNotEqual(type5, BlockType.CODE)
        self.assertNotEqual(type6, BlockType.CODE)
        self.assertNotEqual(type7, BlockType.CODE)
        self.assertNotEqual(type8, BlockType.CODE)
        self.assertNotEqual(type9, BlockType.CODE)
        self.assertNotEqual(type10, BlockType.CODE)
        self.assertNotEqual(type11, BlockType.CODE)


    def test_block_to_block_type_7(self):
        code1 = "``````"
        code2 = "```\n```"
        code3 = "```\n\n```"
        code4 = "```Code```"
        code5 = "```\nCode```"
        code6 = "```Code\n```"
        code7 = "```\nCode\n```"
        code8 = "``` ```"
        code9 = "``` Code ```"

        type1 = BlockMarkDown().block_to_block_type(code1)
        type2 = BlockMarkDown().block_to_block_type(code2)
        type3 = BlockMarkDown().block_to_block_type(code3)
        type4 = BlockMarkDown().block_to_block_type(code4)
        type5 = BlockMarkDown().block_to_block_type(code5)
        type6 = BlockMarkDown().block_to_block_type(code6)
        type7 = BlockMarkDown().block_to_block_type(code7)
        type8 = BlockMarkDown().block_to_block_type(code8)
        type9 = BlockMarkDown().block_to_block_type(code9)
    

        self.assertEqual(type1, BlockType.CODE)
        self.assertEqual(type2, BlockType.CODE)
        self.assertEqual(type3, BlockType.CODE)
        self.assertEqual(type4, BlockType.CODE)
        self.assertEqual(type5, BlockType.CODE)
        self.assertEqual(type6, BlockType.CODE)
        self.assertEqual(type7, BlockType.CODE)
        self.assertEqual(type8, BlockType.CODE)
        self.assertEqual(type9, BlockType.CODE)
        
    
    def test_block_to_block_type_8(self):
        quote1 = ">"
        quote2 = "> "
        quote3 = "> >"
        quote4 = ">>"
        quote5 = "> Quote"
        quote6 = "> Another Quote"
        quote7 = "> \"Quote\""

        type1 = BlockMarkDown().block_to_block_type(quote1)
        type2 = BlockMarkDown().block_to_block_type(quote2)
        type3 = BlockMarkDown().block_to_block_type(quote3)
        type4 = BlockMarkDown().block_to_block_type(quote4)
        type5 = BlockMarkDown().block_to_block_type(quote5)
        type6 = BlockMarkDown().block_to_block_type(quote6)
        type7 = BlockMarkDown().block_to_block_type(quote7)

        self.assertEqual(type1, BlockType.QUOTE)
        self.assertEqual(type2, BlockType.QUOTE)
        self.assertEqual(type3, BlockType.QUOTE)
        self.assertEqual(type4, BlockType.QUOTE)
        self.assertEqual(type5, BlockType.QUOTE)
        self.assertEqual(type6, BlockType.QUOTE)
        self.assertEqual(type7, BlockType.QUOTE)
    

    def test_block_to_block_type_9(self):
        quote1 = " "
        quote2 = "< "
        quote3 = "Quote"
        quote4 = "Another Quote"
        quote5 = "\"Quote\""

        type1 = BlockMarkDown().block_to_block_type(quote1)
        type2 = BlockMarkDown().block_to_block_type(quote2)
        type3 = BlockMarkDown().block_to_block_type(quote3)
        type4 = BlockMarkDown().block_to_block_type(quote4)
        type5 = BlockMarkDown().block_to_block_type(quote5)

        self.assertNotEqual(type1, BlockType.QUOTE)
        self.assertNotEqual(type2, BlockType.QUOTE)
        self.assertNotEqual(type3, BlockType.QUOTE)
        self.assertNotEqual(type4, BlockType.QUOTE)
        self.assertNotEqual(type5, BlockType.QUOTE)
    

    def test_block_to_block_type_10(self):
        list1 = "- Item1"
        list2 = "- Item1\n- Item2"
        list3 = "- \n- "
        list4 = "- Item1\n- "
        list5 = "- \n- Item2"

        type1 = BlockMarkDown().block_to_block_type(list1)
        type2 = BlockMarkDown().block_to_block_type(list2)
        type3 = BlockMarkDown().block_to_block_type(list3)
        type4 = BlockMarkDown().block_to_block_type(list4)
        type5 = BlockMarkDown().block_to_block_type(list5)

        self.assertEqual(type1, BlockType.UNORDERED_LIST)
        self.assertEqual(type2, BlockType.UNORDERED_LIST)
        self.assertEqual(type3, BlockType.UNORDERED_LIST)
        self.assertEqual(type4, BlockType.UNORDERED_LIST)
        self.assertEqual(type5, BlockType.UNORDERED_LIST)
    

    def test_block_to_block_type_11(self):
        list1 = "Item1"
        list2 = "1. Item1"
        list3 = "-Item1"
        list4 = "- Item1\n2.Item2"
        list5 = "- \n-Item2"
        list6 = "- Item1\n-Item2"
        list7 = "Item1\nItem2"
        list8 = "- Item1\n- Item2\n3.Item3"
        list9 = "- Item1\n-"
        list10 = "--Item1"

        type1 = BlockMarkDown().block_to_block_type(list1)
        type2 = BlockMarkDown().block_to_block_type(list2)
        type3 = BlockMarkDown().block_to_block_type(list3)
        type4 = BlockMarkDown().block_to_block_type(list4)
        type5 = BlockMarkDown().block_to_block_type(list5)
        type6 = BlockMarkDown().block_to_block_type(list6)
        type7 = BlockMarkDown().block_to_block_type(list7)
        type8 = BlockMarkDown().block_to_block_type(list8)
        type9 = BlockMarkDown().block_to_block_type(list9)
        type10 = BlockMarkDown().block_to_block_type(list10)

        self.assertNotEqual(type1, BlockType.UNORDERED_LIST)
        self.assertNotEqual(type2, BlockType.UNORDERED_LIST)
        self.assertNotEqual(type3, BlockType.UNORDERED_LIST)
        self.assertNotEqual(type4, BlockType.UNORDERED_LIST)
        self.assertNotEqual(type5, BlockType.UNORDERED_LIST)
        self.assertNotEqual(type6, BlockType.UNORDERED_LIST)
        self.assertNotEqual(type7, BlockType.UNORDERED_LIST)
        self.assertNotEqual(type8, BlockType.UNORDERED_LIST)
        self.assertNotEqual(type9, BlockType.UNORDERED_LIST)
        self.assertNotEqual(type10, BlockType.UNORDERED_LIST)
    

    def test_block_to_block_type_12(self):
        list1 = "1. Item1"
        list2 = "1. Item1\n2. Item2"
        list3 = "1. \n2. "
        list4 = "1. Item1\n2. "
        list5 = "1. \n2. Item2"

        type1 = BlockMarkDown().block_to_block_type(list1)
        type2 = BlockMarkDown().block_to_block_type(list2)
        type3 = BlockMarkDown().block_to_block_type(list3)
        type4 = BlockMarkDown().block_to_block_type(list4)
        type5 = BlockMarkDown().block_to_block_type(list5)

        self.assertEqual(type1, BlockType.ORDERED_LIST)
        self.assertEqual(type2, BlockType.ORDERED_LIST)
        self.assertEqual(type3, BlockType.ORDERED_LIST)
        self.assertEqual(type4, BlockType.ORDERED_LIST)
        self.assertEqual(type5, BlockType.ORDERED_LIST)


    def test_block_to_block_type_13(self):
        list1 = "Item1"
        list2 = "- Item1"
        list3 = "1.Item1"
        list4 = "1. Item1/n2.Item2"
        list5 = "1. /n- Item2"
        list6 = "2. Item1/n3. Item2"
        list7 = "1. Item1/n3. Item2"
        list8 = "1. Item1/n2. Item2/n3.Item3"
        list9 = "1. Item1/n2. Item2/n4. Item3"
        list10 = "1..Item1"

        type1 = BlockMarkDown().block_to_block_type(list1)
        type2 = BlockMarkDown().block_to_block_type(list2)
        type3 = BlockMarkDown().block_to_block_type(list3)
        type4 = BlockMarkDown().block_to_block_type(list4)
        type5 = BlockMarkDown().block_to_block_type(list5)
        type6 = BlockMarkDown().block_to_block_type(list6)
        type7 = BlockMarkDown().block_to_block_type(list7)
        type8 = BlockMarkDown().block_to_block_type(list8)
        type9 = BlockMarkDown().block_to_block_type(list9)
        type10 = BlockMarkDown().block_to_block_type(list10)

        self.assertNotEqual(type1, BlockType.ORDERED_LIST)
        self.assertNotEqual(type2, BlockType.ORDERED_LIST)
        self.assertNotEqual(type3, BlockType.ORDERED_LIST)
        self.assertNotEqual(type4, BlockType.ORDERED_LIST)
        self.assertNotEqual(type5, BlockType.ORDERED_LIST)
        self.assertNotEqual(type6, BlockType.ORDERED_LIST)
        self.assertNotEqual(type7, BlockType.ORDERED_LIST)
        self.assertNotEqual(type8, BlockType.ORDERED_LIST)
        self.assertNotEqual(type9, BlockType.ORDERED_LIST)
        self.assertNotEqual(type10, BlockType.ORDERED_LIST)





    


    

    
    

    

