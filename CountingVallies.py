import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    c=0     #sea level
    v=0     # Number Of Valleys
    for i in path:
        if i=='D':
            c=c-1
        else:
            c=c+1
        if c==0 and i=='U':
            v=v+1
    return(v)
s='UDDDUDUU'    
print(countingValleys(len(s),s))