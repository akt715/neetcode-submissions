class Solution:

    def encode(self, strs: List[str]) -> str:
      arr = []
      for s in strs:
         arr.append(str(len(s)))
         arr.append('#')
         arr.append(s)
      return "".join(arr)

    def decode(self, s: str) -> List[str]:
         l = 0
         res = []
         if len(s) == 0:
            return res
         i = 0
         while  i < len(s):
            if s[i] == '#':
                length = int(s[l:i])
                upto = i+length+1
                decoded_str = s[i+1:upto]
                res.append(decoded_str)
                l = upto
                i = upto
            else:
                i+=1
         
         return res 
