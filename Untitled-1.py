import os
from pathlib import Path
list_delete=[]
def delete_file(path):
    read_file = open("E:\Output\File_list.xls", "r")
    for x in read_file:
        tab_index=x.index('\t')
        file_name=x[:tab_index]
        list_delete.append(file_name)
    read_file.close()
    basepath = path
    for entry in os.listdir(basepath):
        if  os.path.isfile(os.path.join(basepath, entry)):
            if(entry in list_delete):
                os.remove(os.path.join(basepath, entry))

        else:
            path_new = os.path.join(basepath, entry)#if element is a subfolderE:\Test\Test1
            delete_file(path_new)#function is calling itself againE:\Test\Test1

T_path='E:\Test'
list_files=delete_file(T_path)

