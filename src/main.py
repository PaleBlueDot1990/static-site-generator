from copystatictopublic import CopyStaticToPublic
from contentgenerator import ContentGenerator


def main():
    print("Welcome to Static Site Generator!")
    CopyStaticToPublic().delete_and_copy("static", "public")
    ContentGenerator().generate_content("content", "template.html", "public")


if __name__ == "__main__":
    main()