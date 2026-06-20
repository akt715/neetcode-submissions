class Solution:

 def isOneEditDistance(self,s: str, t: str) -> bool:
    m, n = len(s), len(t)

    # Length difference more than 1 → not possible
    if abs(m - n) > 1:
        return False

    # Make sure s is the shorter string
    if m > n:
        return self.isOneEditDistance(t, s)

    i = j = 0
    found_difference = False

    while i < m and j < n:
        if s[i] != t[j]:
            if found_difference:
                return False
            found_difference = True

            # If same length → replace
            if m == n:
                i += 1
        else:
            i += 1
        j += 1

    # If no difference found yet, only valid if extra char exists
    return found_difference or (n - m == 1)

        
        