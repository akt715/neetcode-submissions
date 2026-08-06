class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setOfNumbers = set()

        for n in nums:
            if n in setOfNumbers:
                return True
            setOfNumbers.add(n)
        return False
        
        