class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      map1 = defaultdict(int)
      map2 = defaultdict(int)
      if len(s) != len(t):
          return False

    
      for ch1 in s:
        map1[ch1]+=1
      for ch2 in t:
        map2[ch2]+=1
      
      for k,v in map1.items():
        if map1[k] != map2[k]:
            return False
      
      return True

         