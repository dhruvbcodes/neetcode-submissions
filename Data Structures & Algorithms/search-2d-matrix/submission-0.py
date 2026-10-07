class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix[0])-1

        l2 = 0
        r2 = len(matrix) - 1

        while l2 <= r2:
            row = (l2 + r2) // 2
            if matrix[row][0] <= target and target <= matrix[row][-1]:
                break
            elif matrix[row][0] > target:
                r2 -= 1
            elif matrix[row][-1] < target:
                l2 += 1

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r -= 1
            else:
                l += 1
        
        return False


        
        