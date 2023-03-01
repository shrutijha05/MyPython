def sockMerchant(n, ar):
    d={}
    for i in ar:
        if i not in d:
            d[i]=0
    for i in ar:
        d[i]+=1
    c=0
    for v in d.values():
        c=c+v//2
    return(c)
print(sockMerchant(9, [10,20,20,10,10,30,50,10,20]))