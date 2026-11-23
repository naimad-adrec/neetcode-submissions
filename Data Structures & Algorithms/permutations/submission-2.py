class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []

        used_nums = [False] * len(nums)
        
        def backtrack():
            if len(nums) == len(perm):
                result.append(perm.copy())
                return
            
            for i, num in enumerate(nums):
                if used_nums[i]:
                    continue
                used_nums[i] = True
                perm.append(num)
                backtrack()
                perm.pop()
                used_nums[i] = False
                
            return
        
        backtrack()

        return result
        