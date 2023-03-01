def maxSubArray(nums):
    m = 0
    s = []
    for i in nums:
        if i+m<i:
            m=i
        else:
            m=m+i
        s.append(m)
    return(max(s))

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))