from copystatictopublic import CopyStaticToPublic
from pagegenerator import PageGenerator


def main():
    print("Welcome to Static Site Generator!")
    CopyStaticToPublic().delete_and_copy("static", "public")
    PageGenerator().generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()