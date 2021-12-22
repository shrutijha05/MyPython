def LakeVolume(elevmap):
    v=[]
    i=1
    a=[]
    b=[]
    c=[]
    d=[]
    while (len(elevmap)>i+1):
        if (elevmap[i]<elevmap[i-1]) :
            a.append(i-1)
            c.append(elevmap[i-1])

        if (elevmap[i]<elevmap[i+1]) :
            b.append(i+1)
            d.append(elevmap[i+1])               
        i=i+1
    i=0
    m=c[0]
    while(len(c)>i):
        if (c[i]>=m):
            m=c[i]
            i=i+1
        else:
            a.pop(i)
            m=c.pop(i)
    i=0
    m=d[0]
    while(len(d)>i):
        if b[i]==a[i]:
            b.pop(i)
            d.pop(i)
        elif (d[i]>=m ):
            m=d[i]    
            i=i+1
        else:
            n=b.pop(i)
            m=d.pop(i)
    if len(a)!=len(b):
        b.append(n)
        d.append(m)
    for i in range(0,len(a)):
        v.append(elevmap[a[i]:b[i]+1])
    vol=[]
    for i in v:
        vl=0
        m=min(i[0],i[len(i)-1])
        for x in i[1:len(i)-1]:
            vm=m-x
            vl=vl+vm
        vol.append(vl)
    v=0
    for i in vol:
        v=v+i
    return(v)

ElevMap=[1,4,2,4,1,3,1,4,5,2,2,1,4,2,4]
vol=LakeVolume(ElevMap)
print(vol)