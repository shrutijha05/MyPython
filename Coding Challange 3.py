def initiate_matrix(n):
    a = [ [ '\t' for i in range(n) ] for j in range(n) ]
    print_matrix(a,n)
    return(a)
    
def print_matrix(a,n):
    for i in range(n):
        for j in range(n):
            if(a[i][j]=='\t'):
                print('|',' ',end=' ')
            else:
                print('|',a[i][j],end=' ')
        print('|\n')

def change_val(a,row,col,val):
    a[row][col]=val
    return(a)

def decision(a,n,val):
    des='N'
    l=[]
    count=0
    for i in range(n-1):
        if((a[i][i]==a[i+1][i+1]) and a[i][i]!='\t'):
            count=count+1
    l.append(count)
    count=0
    for i in range(n-1):
        if((a[i][n-i-1]==a[i+1][n-i-2]) and a[i][n-i-1]!='\t'):
            count=count+1
    l.append(count)
    for i in range(n):
        count=0
        for j in range(n-1):
            if((a[i][j]==a[i][j+1]) and a[i][j]!='\t'):
                count=count+1
        l.append(count)
    a = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    for i in range(n):
        count=0
        for j in range(n-1):
            if((a[i][j]==a[i][j+1]) and a[i][j]!='\t'):
                count=count+1
        l.append(count)
    if(max(l)==n-1):
        des=val
    print(des)
    return(des)

def game(a,n,p1,p2):
    count=0
    c=n*n
    des='N'
    while(count<c):
        if(count%2==0):
            inp=input("Player 1 to enter. Please provide the row and then column seperated by comma(both start with 1)\t")
            if(',' not in inp):
                print('Sorry you Entered in wrong Format')
                game(a,n,p1,p2)
            row_str,col_str=inp.split(',')
            row=int(row_str)-1
            col=int(col_str)-1
            if(a[row][col]=='\t'):
                a=change_val(a,row,col,'O')
                print_matrix(a,n)
                des=decision(a,n,'O')
                if(des=='O'):
                    return(des)
            else:
                print('Sorry This Block is Already Filled')
                game(a,n,p1,p2)
        else:
            inp=input("Player 2 to enter. Please provide the row and then column seperated by comma(both start with 1)\t")
            if(',' not in inp):
                print('Sorry you Entered in wrong Format')
                game(a,n,p1,p2)
            row_str,col_str=inp.split(',')
            row=int(row_str)-1
            col=int(col_str)-1
            if(a[row][col]=='\t'):
                a=change_val(a,row,col,'X')
                print_matrix(a,n)
                des=decision(a,n,'X')
                if(des=='X'):
                    return(des)
                
            else:
                print('Sorry This Block is Already Filled')
                game(a,n,p1,p2)
        count=count+1
    return(des)
    
dim=int(input("Enter Dimension of the matrix\t"))
p1=input("Enter the name of First Player (Sign for Player 1 is O)\t")
p2=input("Enter the name of Second Player (Sign for Player 2 is X)\t")
a=initiate_matrix(dim)
d=game(a,dim,p1,p2)
if(d=='O'):
    print('YEAH!!! ',p1,' WON THE GAME')
elif(d=='X'):
    print('YEAH!!! ',p2,' WON THE GAME')
else:
    print('OPPS!!! The Game has ended without any Result')