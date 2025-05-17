import os 
import shutil 

class CopyStaticToPublic():
    def delete_directory(self, path):
        if os.path.isfile(path):
            print(f"Deleting file : {path}")
            os.remove(path)
            return 

        contents = os.listdir(path)
        for content in contents:
            new_path = os.path.join(path, content)
            self.delete_directory(new_path)
        print(f"Deleting direcotry : {path}")
        os.rmdir(path)
        
    
    def copy_directory(self, src_path, des_path):
        if os.path.isfile(src_path):
            print(f"Copying file : {src_path} into file : {des_path}")
            shutil.copy(src_path, des_path)
            return
        
        contents = os.listdir(src_path)
        for content in contents:
            new_src_path = os.path.join(src_path, content)
            new_des_path = os.path.join(des_path, content)

            if os.path.isdir(new_src_path):
                print(f"Creating directory : {new_des_path}")
                os.mkdir(new_des_path)
                
            self.copy_directory(new_src_path, new_des_path)


    def delete_and_copy(self, src_path, des_path):
        self.delete_directory(des_path)
        os.mkdir(des_path)
        self.copy_directory(src_path, des_path)
    












        

        

    


        




