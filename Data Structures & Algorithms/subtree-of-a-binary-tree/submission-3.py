# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def checksub(root, sub):

            if not root and not sub:
                return True

            if not root and sub:
                return False
            
            if root and not sub:
                return False
            
            if root.val != sub.val:
                return False
            
            return (checksub(root.left, sub.left) and                   checksub(root.right,sub.right))

        def dfs(root):

            nonlocal subRoot

            if not root:
                return False
            
            if root.val == subRoot.val:
                if checksub(root, subRoot):
                    return True
                    
            return (dfs(root.left) or dfs(root.right))
        
        return dfs(root)

