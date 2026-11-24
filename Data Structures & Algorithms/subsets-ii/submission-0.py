class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        nums.sort()

        def backtrack(i):
            if i == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            i += 1
            backtrack(i)
            subset.pop()

            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            
            backtrack(i)

            return
        
        backtrack(0)

        return result