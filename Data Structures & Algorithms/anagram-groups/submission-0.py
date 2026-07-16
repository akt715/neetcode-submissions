class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)
        
        for word in strs:
            value = word
            key ="".join(sorted(word))
            map[key].append(value)
        
        res = []

        for k,v in map.items() : 
            res.append(v)
        

        return res