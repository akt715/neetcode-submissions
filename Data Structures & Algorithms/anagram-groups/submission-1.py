class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)
        res =[]
        for s in strs:
            key = ''.join(sorted(s))
            map[key].append(s)
        
        for v in map.values():
            res.append(v)
        
        return res