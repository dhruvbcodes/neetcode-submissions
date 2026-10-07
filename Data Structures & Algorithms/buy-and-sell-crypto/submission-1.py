class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0

        for i in range(len(prices)):
            temp = 0
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    temp = max(temp, prices[j]-prices[i])
            
            res = max(temp,res)
        
        return res

        