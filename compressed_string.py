def decomress(str):
    nstr=''
    i=0
    while(str.count('[')>0):
        if(str[i])==']':
            n=str[0:i+1]
            str=str[i+1:len(str)]
            if (n.count('[')>1):
                i=0
                for x in str:
                    i=i+1
                    if x==']':
                        n=n+str[0:i]
                        str=str[i+1:len(str)]
                        m=1
                        while(m<len(n)):
                            if not (n[0:m].isnumeric()):
                                break
                            m=m+1
                        c=n[0:m-1]
                        n=decomress(n[m:len(n)-1])
                        n=c+'['+n+']'
            x=1
            while(x<len(n)):
                if not (n[0:x].isnumeric()):
                    break
                x=x+1
            i=-1
            m=n[x:-1]
            c=int(n[0:x-1])
            for i in range(0,c):
                nstr=nstr+m

        i=i+1
    return(nstr+str)          

str='2[2[abbb]c]'
res=decomress(str)
tres='abbbabbbcabbbabbbc'
if (res==tres):
    print(True)
else:
    print(False)