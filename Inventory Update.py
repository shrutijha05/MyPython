def str2list(inventory):
    a=[]
    l=[]
    a=list(inventory[2:len(inventory)-2].split("], ["))
    for i in a:
        if i:
            lis1=[]
            lis2=[]
            lis2=list(i.split(", "))
            lis1.append(int(lis2[0]))
            lis1.append(lis2[1][1:-1])
            l.append(lis1)
    return(l)

def update_existing(curInv,newInv):
    for i in range (len(curInv)):
        for j in range (len(newInv)):
            if(curInv[i][1]==newInv[j][1]):
                x=newInv[j][0]+curInv[i][0]
                curInv[i][0]=x
                del newInv[j]
                break
    return(curInv,newInv)

def append_new(curInv,newInv):
    for i in newInv:
        if i:
            curInv.append(i)
    return(curInv)
    
curInv = input('Enter Current Inventory:\n')
newInv = input('Enter New Inventory:\n')
curInv,newInv=update_existing(str2list(curInv),str2list(newInv))
curInv=append_new(curInv,newInv)
print(sorted(curInv,key=lambda x: x[1]))