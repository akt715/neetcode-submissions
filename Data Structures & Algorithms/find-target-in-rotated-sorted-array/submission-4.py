class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

      
        
        while left < right:
            m = (left+right)//2

            if nums[m] >= nums[right]:
                left = m+1
            else:
                right = m
        
        result = self.binarySearch(0,left-1,target,nums) 
        if result >=0:
            return result
        
        return self.binarySearch(left,len(nums)-1,target,nums)
   
        
    def binarySearch (self,l, r,target,nums):
        while l <= r :
            m = (l+r)//2

            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m+1
            else:
                r  = m-1
        return -1
        
            

        