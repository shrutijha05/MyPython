#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    n=len(s)
    a=[]
    for i in range(0,n-m+1):
        a.append([])
        a[i].append(s[i])
        for j in range (i+1,i+m):
            a[i].append(s[j])
    c=0
    for i in a:
        if sum(i)==d:
            c=c+1
    return(c)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    s = map(int, raw_input().rstrip().split())

    first_multiple_input = raw_input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
