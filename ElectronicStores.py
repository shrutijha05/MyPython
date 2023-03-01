import os
import sys
def getMoneySpent(keyboards, drives, b):
    l=[]
    print(keyboards, drives, b)
    for i in keyboards:
        for j in drives:
            n=i+j
            if n<=b:
                l.append(n)
    print(l)
    if l==[]:
        return(-1)
    else:
        return(max(l))

keyboards=[40,50,60]
drives=[5,8,12]
b=60
print(getMoneySpent(keyboards,drives,b))