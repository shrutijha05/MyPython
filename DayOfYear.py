#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if (year==1918):
        s='26.09.'+str(year)
    elif(year<1918):
        if(year%4==0):
            s='12.09.'+str(year)
        else:
            s='13.09.'+str(year)
    else:
        if((year%4==0 and year%100!=0) or (year%400==0)):
            s='12.09.'+str(year)
        else:
            s='13.09.'+str(year)  
            
    return(s)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(raw_input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
