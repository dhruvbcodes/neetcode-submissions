# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ans = True
        def dfs(root):

            nonlocal ans

            if not root:
                return 0
            
            lefth = dfs(root.left)
            righth = dfs(root.right)

            diff = abs(lefth - righth)
            if diff > 1 and ans:
                ans = False

            return 1 + max(lefth,righth)
        
        dfs(root)
        return ans
        