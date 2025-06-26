import sys
from copystatictopublic import CopyStaticToPublic
from contentgenerator import ContentGenerator


def main():
    print("Welcome to Static Site Generator!")

    base_path = "/"
    if len(sys.argv) > 1:
        base_path = sys.argv[1]

    CopyStaticToPublic().delete_and_copy("static", "docs")
    ContentGenerator().generate_content("content", "template.html", "docs", base_path)


if __name__ == "__main__":
    main()