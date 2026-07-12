class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        map = {}
        res = 0
        for i in range(len(s)):
            if s[i] in map and l <= map.get(s[i]):
                l = map.get(s[i])+1
            map[s[i]] = i
            res = max(res, i-l+1) 
        return res