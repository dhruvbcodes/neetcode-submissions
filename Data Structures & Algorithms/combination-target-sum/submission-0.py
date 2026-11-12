class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        def sub(i, s, curr):

            if s == target:
                res.append(curr.copy())
                return None
            
            if i >= len(nums) or s > target:
                return None        
            
            curr.append(nums[i])
            sub(i, s + nums[i], curr)
            curr.pop()
            sub(i + 1, s, curr)
        
        sub(0, 0, [])
        return res