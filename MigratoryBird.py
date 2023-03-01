#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    d=dict()
    for i in arr:
        if i not in d:
            d[i]=0
    for i in arr:
        d[i]=d[i]+1
    c=0
    m=[]
    for x,y in d.items():
        if y==c:
            c=y
            m.append(x)
        elif(y>c):
            c=y
            m=[x]
    return(min(m))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
