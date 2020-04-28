n=input("Enter a string:\t")
a=0
for i in range (len(n)):
    if(n[i].lower()!=n[(len(n))-1-i].lower()):
        a=a+1
        

if(a==0):
    print("String is Palindrome")
else:
    print("String is not Palindrome")
