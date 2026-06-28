class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            m = (left+right)//2

            if nums[m] > nums[right]:
                left = m+1
            else:
                right = m


        start = right 
        end = right -1 
        left = 0
        right = len(nums)-1

        while left <= end :
            m = (left+end)//2

            if nums[m] == target:
                return m
            if nums[m] > target:
                end = m-1
            else:
                left = m + 1
        

        while start <= right:
            m = (start+right)//2
            if nums[m] == target:
                return m
            if nums[m] > target:
                right = m-1
            else:
               start = m + 1
        
        return -1
        
            

        