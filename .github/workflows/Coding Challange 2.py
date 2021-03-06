import string
import time
lis=[]
def count_replace(beginWord,endWord,wordList,count):                    #Fxn to count
    for i in string.ascii_lowercase:                                    #change each letter in the
        for x in range(len(beginWord)):                                 #To check each letters of word                                 
            s1=list(beginWord)                                          #Convert string to list as string is intangible
            s1[x]=i                                                     #change one letter of the word
            l="".join(s1)
            if not wordList:                                            #if wordlist is empty then return
                return

            else:
                if(l==endWord):                                         #if changed word is end word
                    count=count+1                                       #increase the count
                    if wordList:                                        #if wordlist is not empty
                        print(count)                                    #print Count
                        lis.append(count)                               #append count in the list to signify end word had reached
                        return 
                elif(l in wordList):                                    #else if word is in word list
                    count=count+1                                       #increase the count             
                    wordList.pop(wordList.index(l))                     #pop the word from the word list
                    if (len(wordList)>=2):                              #if wordlist has more then 1 word other then end word
                        count_replace(l,endWord,wordList,count)         #recursion of the function
                    else:
                        if not lis:                                     #if endword cannot be reached
                            print(0)                                    #print 0                           
        
t1=time.time()                                                          #initial time
beginWord = "hit"
endWord = "cog"
count=1                                                                 #initial count
wordList = ["hot","dot","dog","lot","log","cog"]
if (endWord in wordList):                                               #if endword is in wordlist
    count_replace(beginWord,endWord,wordList,count)                     #calling the function
else:
    print(0)                                                            #if endword is not in wordlist print 0
t2=time.time()                                                          #final time
t=(t2-t1)                                                               #time taken
print("Time Complexity of the program",t)                               #print total time taken