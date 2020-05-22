def str2lis(lis):
    a=[]
    l=[]
    a=list(lis[1:len(lis)-1].split(","))
    for i in a:
        l.append(int(i))
    return(l)
def sym(args):
    a1=args.pop()
    a2=args.pop()
    l=[]
    for i in a1:
        if((i not in a2) and (i not in l)):
            l.append(i)
    for i in a2:
        if((i not in a1) and (i not in l)):
            l.append(i)
    args.append(sorted(l))
    if(len(args)>1):
        s=sym(args)
        return(s)
    else:
        return(args[0])
    
l=[]
n=input('Enter Number of Arrays you want to enter:\t')
for i in range(int(n)):
    l.append(str2lis(input('Enter the set of Element:\t')))
s=sym(l)
print(s)