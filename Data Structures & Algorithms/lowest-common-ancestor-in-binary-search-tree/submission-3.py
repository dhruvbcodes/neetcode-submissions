# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        visited = set()
        ans = None

        def dfs(root, p, q):

            nonlocal ans

            if not root:
                return 0
            
            left = dfs(root.left,p,q)
            right = dfs(root.right,p,q)                
            
            total = left + right
               
            if total == 1 and (root == p or root == q):
                ans = root

            if total == 2 and not ans:
                ans = root
            
            if root == p or root == q:
                return 1

            return total
        
        dfs(root,p,q)

        return ans


        