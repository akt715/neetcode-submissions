class Solution:

 def isOneEditDistance(self,s: str, t: str) -> bool:
    n = len(s)
    m = len(t)
    if abs(m - n) > 1:
        return False

    if n > m:
        return self.isOneEditDistance(t, s)
    left= 0
    right = 0
    is_difference = False

    while  left < n and right < m:
        if s[left] != t[right]:
            if is_difference:
                return False
            is_difference = True
            if m == n:
                left += 1
        else:
            left+=1
        right+=1
        
    return is_difference or abs(m-n)==1

        
        