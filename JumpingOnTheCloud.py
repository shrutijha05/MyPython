def jumpingOnClouds(c, k):
    i=(k%len(c))
    e=99
    if (c[i]==1):
        e=e-2
    while(i>0 and e>0):
        i=(i+k)%len(c)
        e=e-1
        if (c[i]==1):
            e=e-2
    return(e)

print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0],2))