class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                sum = nums[i]+nums[l]+nums[r]
                if l > i+1 and nums[l] == nums[l-1]:
                    l = l+1
                    continue
                if sum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l = l+1
                    r = r-1
                elif sum > 0:
                    r = r-1
                else:
                    l = l+1
        
        return res 