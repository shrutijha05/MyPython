import time
def verify_parenthesis(string_passed):
    s=string_passed
    res='TRUE'
    st=[]
    for i in range(len(s)):
        if (s[i] in ['(','[','{']):
            st.append(s[i])
        elif(s[i] in [')',']','}']):
            if (not st):
                res='False'
                break
            n=st.pop()
            if(s[i]==')'):
                if(n!='('):
                    res='FALSE'
            elif(s[i]==']'):
                if(n!='['):
                    res='FALSE'
            elif(s[i]=='}'):
                if(n!='{'):
                    res='FALSE'
        else:
            res='False'
            break
    if(st):
        res='FALSE'
    return res
t1=time.time()
s=input("Enter the Paranthesis:\t\t")
result=verify_parenthesis(s)
print(result)
t2=time.time()
t=(t2-t1)
print("Time Complexity of the program",t)
