def FindIntersection(strArr):
      arr=[]
      s=''
      for i in strArr:
        arr.append(i.split(', '))
      for i in arr[0]:
        if i in arr[1]:
          s=s+i+','
      strArr=s[:-1]
      if strArr=='':
        strArr='false'
      
      
      # code goes here
      return strArr

# keep this function call here 
print(FindIntersection(input()))