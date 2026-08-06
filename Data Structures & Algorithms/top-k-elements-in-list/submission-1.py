class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        freqList = [[] for i in range(len(nums)+1)]
        res = []
        for n in nums:
            freqMap[n]+=1
        
        for key,value in freqMap.items():
            freqList[value].append(key)
        
        for i in range(len(freqList)-1,-1,-1):
            for n in freqList[i]:
                if k == 0:
                    return res
                k-=1
                res.append(n)
        
        return res
                



