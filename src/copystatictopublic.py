import os 
import shutil 

class CopyStaticToPublic():
    def delete_directory(self, path):
        if os.path.isfile(path):
            os.remove(path)
            return 

        contents = os.listdir(path)
        for content in contents:
            new_path = os.path.join(path, content)
            self.delete_directory(new_path)
        os.rmdir(path)
        
    
    def copy_directory(self, src_path, des_path):
        if os.path.isfile(src_path):
            shutil.copy(src_path, des_path)
            return
        
        contents = os.listdir(src_path)
        for content in contents:
            new_src_path = os.path.join(src_path, content)
            new_des_path = os.path.join(des_path, content)

            if os.path.isdir(new_src_path):
                os.mkdir(new_des_path)
                
            self.copy_directory(new_src_path, new_des_path)


    def delete_and_copy(self, src_path, des_path):
        print(f"\nDeleting all subdirectories and files from directory: \'{des_path}\' recursively.")
        self.delete_directory(des_path)
        os.mkdir(des_path)
        print(f"Finished deleting.")

        print(f"Copying static contents of directory: \'{src_path}\' in directory: \'{des_path}\'.")
        self.copy_directory(src_path, des_path)
        print(f"Finished copying.\n")

    












        

        

    


        




