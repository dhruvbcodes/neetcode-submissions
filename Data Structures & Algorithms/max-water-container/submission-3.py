class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i, j = 0, len(heights)-1
        res = 0

        while i < j:
            h = min(heights[i],heights[j])
            tot = h * (j-i)
            if tot > res:
                res = tot
            
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return res
        