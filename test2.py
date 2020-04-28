import os
from pathlib import Path
import platform
from datetime import datetime
from datetime import date
list_of_files=[]
def get_file(path):#Function
    basepath = path
    for entry in os.listdir(basepath):
        if  os.path.isfile(os.path.join(basepath, entry)):
            t=os.path.getctime(os.path.join(basepath, entry))
            d = datetime.utcfromtimestamp(t)
            today = datetime.today()
            day=(today-d).days
            if(day>=15):
                list_of_files.append(entry)

        else:
            path_new = os.path.join(basepath, entry)
            get_file(path_new)
    
    return (list_of_files)
    

list_files=get_file('E:\Test')#give your path here 
print(list_files)# you will get the list of file here
