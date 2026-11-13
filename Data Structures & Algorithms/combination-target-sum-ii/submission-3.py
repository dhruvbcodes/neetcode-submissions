class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        nums = sorted(candidates)
        
        def sub(i, s, curr):

            if s == target:
                res.append(curr.copy())
                return None
            
            if s > target or i >= len(nums):
                return None
            
            for j in range(i,len(nums)):

                if j > i and nums[j] == nums[j-1]:
                    continue
                
                if nums[j] > target - s:
                    return None

                curr.append(nums[j])
                sub(j+1, s + nums[j], curr)
                curr.pop()  

        sub(0, 0, [])
        return res
        