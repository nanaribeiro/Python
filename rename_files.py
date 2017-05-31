import os
#import re
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"D:\WebDev\prank")
    saved_path = os.getcwd() #gets the current directory path 
    #change the working directory to the directory we need 
    os.chdir(r"D:\WebDev\prank")
    #(2) for each file, rename filename
    for file_name in file_list:
        #translateTab = maketrans(
        os.rename(file_name, file_name.translate({ord(ch): None for ch in "0123456789"}))
        # It can use re.sub('[0-9]+', '', file_name) instead of translate
    os.chdir(saved_path)
rename_files()
    
