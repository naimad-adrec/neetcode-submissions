# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None

        def dfs(node):
            nonlocal result, k
            if result:
                return
            
            if node.left:
                dfs(node.left)
            
            if k == 1 and result is None:
                result = node.val
                return
            
            k -= 1
            
            if node.right:
                dfs(node.right)
            
            return
        
        dfs(root)

        return result
        