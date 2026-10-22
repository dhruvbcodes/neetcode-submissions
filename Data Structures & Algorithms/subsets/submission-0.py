class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def sub(i, curr):

            if i >= len(nums):
                res.append(curr.copy())
                return None
            
            curr.append(nums[i])
            sub(i+1, curr)
            curr.pop()
            sub(i+1, curr)

            return curr

        sub(0, [])
        
        return res

            
            
        