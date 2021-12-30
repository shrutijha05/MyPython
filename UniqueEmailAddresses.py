class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        l=set()
        for i in emails:
            x=i.split('@')
            x[0]=x[0].replace('.','')
            if '+' in x[0]:
                x[0]=x[0][:x[0].index('+')]
            l.add(x[0]+'@'+x[1])
        return(len(l))   