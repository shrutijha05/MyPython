def maxsubsequence(W1,W2):
    m=len(W1)
    n=len(W2)
    X=[[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                X[i][j] = 0
            elif W1[i-1] == W2[j-1]:
                X[i][j] = X[i-1][j-1] + 1
            else:
                X[i][j] = max(X[i-1][j], X[i][j-1])

    index = X[m][n]
    return(index)

def longestword(S,D):
    c=0
    for i in D:
        r=maxsubsequence(i,S)
        if c<r:
            c=r
            long=i
    return(long)
    
S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}
longest=longestword(S,D)
print(longest)