class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        lookup = set(nums)
        res = 0
        for n in nums:
            if n-1 not in lookup:
                l = 0
                while (n+l) in lookup:
                    l += 1
                if l >= res:
                    res = l
        
        return res


        