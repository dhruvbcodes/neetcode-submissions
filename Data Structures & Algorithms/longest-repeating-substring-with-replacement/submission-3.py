class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        i = 0
        count = defaultdict(int)
        res = 0
        maxf = 0
        
        for j in range(len(s)):
            if s[j] in count:
                count[s[j]] += 1
            else:
                count[s[j]] = 1
            
            maxf = max(maxf,count[s[j]])

            freq = (j - i + 1) - maxf
            if freq <= k:
                res = max(res, maxf+freq)    
            else:
                count[s[i]] -= 1
                i += 1

        
        return res


        