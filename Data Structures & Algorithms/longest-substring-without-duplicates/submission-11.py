class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        i = 0
        count = set()

        for j in range(len(s)):
            while s[j] in count:
                count.remove(s[i])
                i += 1
            count.add(s[j])
            res = max(res, j - i + 1)
        
        return res 

