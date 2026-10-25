class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        res = 0
      
        for ch in charSet:
            l = 0
            count = k
            for i in range(len(s)):
                if s[i] != ch:
                    count-=1
                while l <= len(s)-1 and count<0:
                    if s[l]!=ch:
                        count+=1
                    l+=1
                res = max(res, i-l+1)
        
        return res 


