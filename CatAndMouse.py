def catAndMouse(x, y, z):
    a=abs(z-x)
    b=abs(z-y)
    if a>b:
        return('Cat B')
    elif(b>a):
        return('Cat A')
    else:
        return('Mouse C')
print(catAndMouse(1,3,2))