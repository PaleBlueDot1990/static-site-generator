from textnode import TextType, TextNode
from htmlnode import HTMLNode
from inlinemarkdown import InlineMarkdown
from blockmarkdown import BlockMarkDown


def main():
    print("Welcome to Static Site Generator!")

    md = """
# **This is heading 1**

_This is a paragraph
with a second line
and with a third line_

> This is a `quote`

1. **Ordered** List _Item 1_
2. **Ordered** List _Item 2_
3. **Ordered** List _Item 3_

- **Unordered** List _Item 1_
- **Unordered** List _Item 2_
- **Unordered** List _Item 3_
"""

    node = BlockMarkDown().markdown_to_html_node(md)
    html = node.to_html()
    print(html)
    
    
if __name__ == "__main__":
    main()