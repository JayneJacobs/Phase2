# Open the directory containing the files
#Rename the files until they do not have numbers.
        # look at the file name, find the number
        #delete the numbers
        #name the file with the remaining characters.
import os

    # 1 get all file names
def rename_files():
    file_name_path = os.getcwd()
    print(file_name_path,"this is where we are now")
    #myDir = 'r"' + file_name_path + '"'
    myDir = file_name_path 
    os.chdir(myDir)
    file_list = os.listdir(myDir)
    print myDir
    print(file_list)                
    # 2 for each file
    #Rename files
    #new = ''
    
    #mindSquares
    #os.chdir(myDir)
    for file_name in file_list:
        file_name_path = os.getcwd()
        #os.chdir(myDir)
        #os.rename(file_name, file_name.translate(None,"0123456789"))
        print(file_name_path,"this is where we are in a loop")
    os.chdir(myDir)
    file_list = os.listdir(myDir)
    #return file_list
    #mindSquares

print(rename_files(),"after running")

#import mindSquares


                           
    
              

              

              
