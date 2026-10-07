class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        res = float('inf')

        while l <= r:

            k = (l + r) // 2
            t = 0
            for i in range(len(piles)):
                t += math.ceil(piles[i]/ k)
            
            if t <= h and k <= res:
                res = k
                r = k - 1
            elif t > h:
                l = k + 1
                    
        return res