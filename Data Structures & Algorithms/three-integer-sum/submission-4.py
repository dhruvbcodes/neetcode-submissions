class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            l = 0
            r = len(nums)-1
            while l < i and r > i and l < r:
                sum = nums[l] + nums[r] + nums[i]
                if sum == 0:
                    res.add((nums[l],nums[r],nums[i]))
                    r -= 1
                    l += 1
                if sum > 0:
                    r -= 1
                if sum < 0:
                    l += 1
        
        return list(res)