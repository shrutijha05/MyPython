import numpy as np
def Squaretrue(Words):
    T=True
    k=len(Words)
    for i in Words:
        if len(i)!=k:
            T=False
            break
    w=[]
    for i in Words:
        w.append(list(i))
    w=np.array(w)
    wt=w.transpose()
    T=np.array_equal(w,wt)
    return(T)
   
def wordSequence(W):
    l=[]
    n=len(W)
    sum=0
    W=sorted(W)
    for i in range(0,n):
        for j in range (0,n):
            for x in range (0,n):
                for y in range(0,n):
                    if((i!=j)and(i!=x)and (i!=y)and (j!=x) and (j!=y) and (x!=y)):
                        l.append([W[i],W[j],W[x],W[y]])
    lis=[]
    for i in l:
        if(Squaretrue(i)):
            lis.append(i)
    print(lis)

W=["abat","baba","atan","atal"]
wordSequence(W)