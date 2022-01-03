#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    if n%2!=0:
        return(min((p//2),(n-p)//2))
    else:
        return(min((p//2),(n-p+1)//2))
            
        

print(pageCount(6,5))