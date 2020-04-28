a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x=[]
for i in range(0,len(a)):
    for j in range(i,len(b)):
        if a[i]==b[j]:
            x.append(a[i])

print(x)

