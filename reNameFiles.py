# Open the directory containing the files
#Rename the files until they do not have numbers.
        # look at the file name, find the number
        #delete the numbers
        #name the file with the remaining characters.
import os

    # 1 get all file names
def rename_files():
    file_list = os.listdir(r"C:\LocalDocuments\Programing\Python\projects\PythonHomeGrown\Phase2\prank")
    print(file_list)                
    # 2 for each file
    #Rename files
    #new = ''
    file_name_path = os.getcwd()
    print(file_name_path,"this is where we are now")
    os.chdir(r"C:\LocalDocuments\Programing\Python\projects\PythonHomeGrown\Phase2\prank")
    # 
    for file_name in file_list:
        #old = file_name
        #new = file_name.translate(None,"0123456789")
        os.rename(file_name, file_name.translate(None,"0123456789"))
        #print(file_name_path,"this is where we are in a loop")
    os.chdir(file_name_path)
    file_list = os.listdir(r"C:\LocalDocuments\Programing\Python\projects\PythonHomeGrown\Phase2\prank")
    return file_list

print(rename_files(),"after running")
                           
    
              

              

              
