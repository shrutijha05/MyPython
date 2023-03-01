def join(a,b,c):
    join=[]
    i=0
    j=0
    if len(a)>len(b):
        while(j<len(b)):
            for x in (a[i:i+c]):
                join.append(x)
            join.append(b[j])
            j=j+1
            i=i+c
        for i in a[i:len(a)]:
            join.append(i)
    else:
        while(j<len(a)):
            for x in (a[i:i+c]):
                join.append(x)
            join.append(b[j])
            j=j+1
            i=i+c
        for i in b[i:len(b)]:
            join.append(i)
    return(join)

def flatten(arr):
    c=0
    jarr=[]
    for i in arr:
        jarr=join(jarr,i,c)
        c=c+1
    print(jarr)
arr1 = [1, 2, 3]
arr2 = [4, 5]
arr3 = [6, 7, 8, 9];
a=[arr1]
flatten(a)    