import numpy as np
import random
def minesweeper(r,c,n):
    M=np.zeros((r,c), dtype=np.int)
    l1=random.sample(range(0,r-1),n)
    l2=random.sample(range(0,c-1),n)
    for i in range(0,n):
        M[l1[i]][l2[i]]=9
    M=np.pad(M,((1,1),(1,1)), 'constant')
    for i in range(1,r+1):
        for j in range (1,c+1):
            m=M[i-1:i+2,j-1:j+2]
            if (m[1][1]!=9):
                m[1][1]=0
            count=np.count_nonzero(m == 9)
            if (M[i][j]!=9):
                M[i][j]=count
    M=M[1:-1,1:-1]
    return(M)

Mine=minesweeper(12, 10, 7)
print(Mine)