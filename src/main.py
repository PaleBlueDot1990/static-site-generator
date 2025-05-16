from textnode import TextType, TextNode
from htmlnode import HTMLNode
from inlinemarkdown import InlineMarkdown
from blockmarkdown import BlockMarkDown


def main():
    print("Welcome to Static Site Generator!")

    md = """
# This is heading 1

This is a paragraph
with a second line
and with a third line

## This is heading 2

> This is a quote

### This is heading 3

```
This is a code block
with some code snippets
```

#### This is heading 4

1. Ordered List Item 1
2. Ordered List Item 2
3. Ordered List Item 3

##### This is heading 5

- Unrdered List Item 1
- Unordered List Item 2
- Unordered List Item 3
"""

    node = BlockMarkDown().markdown_to_html_node(md)
    html = node.to_html()
    print(html)
    
    
if __name__ == "__main__":
    main()