import os
from blockmarkdown import BlockMarkDown

class PageGenerator():
    def extract_title(self, markdown):
        lines = markdown.split("\n")

        for line in lines:
            if line.startswith("# "):
                title_text = line[2:].strip()
                return title_text
        
        raise ValueError("Heading not found in the markdown file")
    
    def generate_page(self, src_file_path, template_path, dest_file_path):
        print("\n-----------------------------------------------")
        print(f"Generating page from {src_file_path} to {dest_file_path}")

        with open(src_file_path, 'r', encoding = 'utf-8') as file:
            markdown = file.read()
        
        page_content = BlockMarkDown().markdown_to_html_node(markdown).to_html()
        page_title = self.extract_title(markdown)
        
        with open(template_path, 'r', encoding = 'utf-8') as file:
            page_template = file.read()
        
        page = page_template.replace("{{ Title }}", page_title).replace("{{ Content }}", page_content)

        with open(dest_file_path, 'w', encoding = 'utf-8') as file:
            file.write(page)
        
        print(f"Page generated successfully at {dest_file_path}")
        print("\n-----------------------------------------------")
    

    def generate_pages_recursive(self, src_path, template_path, dest_path):
        if os.path.isfile(src_path):
            self.generate_page(src_path, template_path, dest_path)
            return 
        
        contents = os.listdir(src_path)
        for content in contents:
            new_src_path = os.path.join(src_path, content)

            if os.path.isdir(new_src_path):
                new_dest_path = os.path.join(dest_path, content)
                os.mkdir(new_dest_path)
            else:
                new_dest_path = os.path.join(dest_path, content.split('.')[0] + ".html")

            self.generate_pages_recursive(new_src_path, template_path, new_dest_path)
            





        

        

        



        
        





    


        

    

        


