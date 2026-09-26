class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for n in nums:
            if n-1 not in numSet:
                count=0
                while n in numSet:
                    n+=1
                    count+=1
                    res = max(count,res)
        
        return res