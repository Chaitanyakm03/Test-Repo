

import os
import shutil

file_path="G:\\one\\read\\New.txt"
file_search_path="G:\\Two"

with open(file_path,"r")as file:
    first_line = file.readline()
    value=first_line.split(":")[1].strip()
    directories=os.listdir(file_search_path)
    for dir in directories:
        if dir == value:
            dir_path = os.path.join(file_search_path,value)
            dest=dir_path+"copy"
            shutil.copytree(dir_path,dest)
'''
import os
import shutil
import fnmatch

original = r"G:\one\read"
target = r"G:\Two"

pattern = '"New.txt"'

src_files = os.listdir(original)

for file_name in src_files:

    if fnmatch.fnmatch(file_name,
'''
