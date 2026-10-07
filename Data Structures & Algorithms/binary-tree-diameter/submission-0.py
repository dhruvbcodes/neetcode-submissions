# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        currd = 0
        def dfs(root):

            nonlocal currd

            if root is None:
                return 0
            
            rightl = dfs(root.right)
            leftl = dfs(root.left)

            currd = max(currd, rightl + leftl)

            return 1 + max(rightl, leftl)
        
        dfs(root)

        return currd
        