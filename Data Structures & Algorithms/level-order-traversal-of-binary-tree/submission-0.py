# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        def bfs(root):

            if root is None:
                return []

            queue = deque([root])

            while queue:

                siz = len(queue)
                curr_lvl = []

                for _ in range(siz):

                    curr = queue.popleft()
                    curr_lvl.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)
                    
                    if curr.right:
                        queue.append(curr.right)
                
                res.append(curr_lvl)
        
        bfs(root)
        return res
        