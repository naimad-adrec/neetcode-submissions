class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(subset, i):
            nonlocal result
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            backtrack(subset, i + 1)
            subset.pop()

            backtrack(subset, i + 1)

            return
        
        backtrack([], 0)

        return result
        