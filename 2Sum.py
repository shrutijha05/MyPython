class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i,j in enumerate(nums):
            seen[j] = i
        for i,j in enumerate(nums):
            num = target - j
            if num in seen and i!=seen[num]:
                return [i,seen[num]]