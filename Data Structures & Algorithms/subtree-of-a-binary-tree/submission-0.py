# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def isSameTree(node, subNode):
            if not node and not subNode:
                return True
            elif not node or not subNode or node.val != subNode.val:
                return False
            
            return isSameTree(node.left, subNode.left) and isSameTree(node.right, subNode.right)
        
        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        