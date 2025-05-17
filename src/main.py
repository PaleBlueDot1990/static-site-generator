from textnode import TextType, TextNode
from htmlnode import HTMLNode
from inlinemarkdown import InlineMarkdown
from blockmarkdown import BlockMarkDown
from copystatictopublic import CopyStaticToPublic


def main():
    print("Welcome to Static Site Generator!")
    CopyStaticToPublic().delete_and_copy("static", "public")


if __name__ == "__main__":
    main()