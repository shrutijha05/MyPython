def miniMaxSum(arr):
    # Write your code here
    a=[]
    for i in arr:
        a.append(sum(arr)-i)
    a=[min(a),max(a)]
    return(a)
    
a=(miniMaxSum([1,2,3,4,5]))
print(*a)