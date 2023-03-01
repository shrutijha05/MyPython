class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        slist=set()
        nums=sorted(nums)
        n=len(nums)
        for i in range(0,n-3):
            for j in range(i+1,n-2):
                su=nums[i]+nums[j]
                s=target-su
                l=j+1
                r=n-1
                while(l<r):
                    if(s==nums[l]+nums[r]):
                        slist.add((nums[i],nums[j],nums[l],nums[r]))
                        l=l+1
                        r=r-1
                    elif (s<nums[l]+nums[r]):
                        r=r-1
                    else:
                        l=l+1
        return(slist)
                        
        