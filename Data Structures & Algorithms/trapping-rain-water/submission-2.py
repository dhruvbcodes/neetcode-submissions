class Solution:
    def trap(self, height: List[int]) -> int:

        maxh = [0] * len(height)
        maxh[-1] = height[-1]

        for i in range(len(height) - 2, -1, -1):
            maxh[i] = max(maxh[i + 1], height[i + 1])

        tot = 0
        left_max = height[0]

        for i in range(1, len(height) - 1):
            water = min(left_max, maxh[i]) - height[i]

            if water > 0:
                tot += water

            left_max = max(left_max, height[i])

        return tot
