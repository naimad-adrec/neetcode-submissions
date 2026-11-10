class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            i += 1
            backtrack(i)
            subset.pop()
            backtrack(i)

            return
        
        backtrack(0)

        return result
        