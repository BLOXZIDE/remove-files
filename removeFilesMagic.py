from importlib.resources import path
import os
import shutil
import time

def main():
    path = "/Users/HP18/Desktop/Adi"
    days = 5
    second = time.time() - (days * 60*24*60) 

    if os.path.exists(path):
        for root_folder, folders,files in os.walk(path):
            if second >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                    if second >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
            
            for file in files:
                file_path = os.path.join(root_folder, file)
                if second >= get_file_or_folder_age(file_path):
                    remove_file(file_path)
                else:
                    if second >= get_file_or_folder_age(path):
                        remove_file(path)
				


def remove_folder(path):


	if not shutil.rmtree(path):


		print(f"{path} is removed successfully")

	else:


		print(f"Unable to delete the "+path)



def remove_file(path):


	if not os.remove(path):


		print(f"{path} is removed successfully")

	else:


		print("Unable to delete the "+path)


def get_file_or_folder_age(path):

	
	ctime = os.stat(path).st_ctime


	return ctime



	main()