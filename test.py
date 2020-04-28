def Write_File(list_passed):
        list_files=list_passed
        with open('E:\Output\File_list.xls', "w") as myfile:
                for l in list_files:
                        myfile.write("%s\t" % l)
                        if ((list_files.index(l)%2)!=0):
                                myfile.write("\n