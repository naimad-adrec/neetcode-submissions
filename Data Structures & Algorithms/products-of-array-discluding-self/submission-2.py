class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        result = [1] * nums_len
        for i in range(1, nums_len):
            result[i] = nums[i - 1] * result[i - 1]
        
        postfix = [1] * nums_len
        for i in range(nums_len - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]
            result[i] = result[i] * postfix[i]
        
        return result
