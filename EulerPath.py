from collections import deque
x={0:[6,1],1:[2],2:[3,0],3:[4],4:[5,2],5:[0],6:[4]}
a=deque()
b=deque()
c=[]
#Start from First element
n=list(x.keys())[0]
a.append(n)

while(len(x)>0):
    if n in b:
        s=a.pop()
        b.append(s)
        if(len(a)>0):
            n=a[-1]
        else:
            break
    elif(len(x[n])==0):
        x.pop(n)
        s=a.pop()
        b.append(s)
        n=a[-1]
        if n in b:
            s=a.pop()
            b.append(s)
            if(len(a)>0):
                n=a[-1]
            else:
                break
    else:
        s=x[n].pop(0)
        n=s
        a.append(n)

while(len(a)>0):
    s=a.pop()
    b.append(s)

while(len(b)>0):
    s=b.pop()
    c.append(s)
print(c)