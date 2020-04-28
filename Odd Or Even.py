n=input("Enter any number:\t")
n1=input("Enter another number:\t")
m=int(n)%2
x=int(n)%4
y=int(n)/int(n1)
if (m==1):
    print("The Number",n,"is odd")
else:
    print("The Number",n,"is even") 
if (x==0):
    print("The Number",n,"is divided by 4")
else:
    print("The Number",n,"is not divided by 4") 
if (y==0):
    print("The Number",n,"is divided by the number",n1)
else:
    print("The Number",n,"is not divided by the number",n1) 