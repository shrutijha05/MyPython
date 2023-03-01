def birthdayCakeCandles(candles):
    # Write your code here
    c=0
    m=max(candles)
    for i in candles:
        if (m==i):
            c=c+1
    return(c)

print(birthdayCakeCandles([4,4,1,3]))