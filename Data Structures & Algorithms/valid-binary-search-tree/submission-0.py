# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return [True, float('inf'), float('-inf')]
            
            left_result = helper(node.left)
            right_result = helper(node.right)

            if left_result[0] and right_result[0] and node.val > left_result[2] and node.val < right_result[1]:
                min_val = node.val if left_result[1] == float('inf') else left_result[1]
                max_val = node.val if right_result[2] == float('-inf') else right_result[2]

                return [True, min_val, max_val]
            
            return [False, left_result[1], right_result[2]]
        
        return helper(root)[0]
        