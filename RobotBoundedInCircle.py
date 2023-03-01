class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d=0
        p=[0,0]
        for i in instructions:
            if i=='L':
                d=(d+3)%4
            elif i=='R':
                d=(d+1)%4
            else:
                if d==0:
                    p[1]=p[1]+1 
                elif d==2:
                    p[1]=p[1]-1   
                elif d==3:
                    p[0]=p[0]+1
                else:
                    p[0]=p[0]-1
        if p==[0,0] or d!=0:
            return(True)    