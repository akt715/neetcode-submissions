class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map:
                res.append(map[diff])
                res.append(i)
                return res
            map[nums[i]] = i
        
        return res
