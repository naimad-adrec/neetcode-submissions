# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
        def helper(node) -> int:
            if not node:
                return [True, 0]

            left_result = helper(node.left)
            right_result = helper(node.right)
            depth = 1 + max(left_result[1], right_result[1])
            is_balanced = left_result[0] and right_result[0] and abs(left_result[1] - right_result[1]) <= 1

            return [is_balanced, depth]
        
        return helper(root)[0]
        