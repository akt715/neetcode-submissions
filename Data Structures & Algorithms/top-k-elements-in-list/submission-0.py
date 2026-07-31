class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for n in nums:
            map[n]+=1
        heap = []
        for key,v in map.items():
            heapq.heappush(heap,((-1)*v , key ))
        
        res = []
        while heap and k>0:
            k-=1
            t = heapq.heappop(heap)
            res.append(t[1])
        
        return res
