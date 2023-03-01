import sys
d=dict()
inp=sys.stdin.read()
inp=inp.split('\n')
n=int(inp[0])
for i in inp[1:n+1]:
    x=i.split(' ')
    d[x[0]]=x[1]
for i in inp[n+1:]:
    if i in d:
        a=''
        a=i+'='+d[i]
        print(a)
    else:
        print('Not found')
