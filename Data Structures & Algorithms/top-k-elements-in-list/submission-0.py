class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        pq = []
        for i in count.keys():
            heapq.heappush(pq,(-(count[i]),i))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(pq)[1])     

        return res   