class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = nums[i - 1] * result[i - 1]
        
        postfix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]
            result[i] = result[i] * postfix[i]
        
        return result
