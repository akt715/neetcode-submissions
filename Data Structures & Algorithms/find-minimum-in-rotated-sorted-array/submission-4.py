class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')

        left = 0
        right = len(nums)-1

       
        while left <= right:
            if nums[left] < nums[right]:
                return min(res,nums[left])
      
            m = (left+right)//2
            res = min(nums[m],res)

            if  nums[m] >= nums[left]:
                  left = m+1
            else:
                  right = m-1
        return res