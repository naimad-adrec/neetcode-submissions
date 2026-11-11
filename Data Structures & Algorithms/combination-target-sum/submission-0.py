class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        result = []
        combination = []
        def backtrack(i, curr_sum):
            if i >= len(nums) or curr_sum >= target:
                if curr_sum == target:
                    result.append(combination.copy())
                return

            backtrack(i + 1, curr_sum)
            
            combination.append(nums[i])
            backtrack(i, curr_sum + nums[i])
            combination.pop()

            return

        backtrack(0, 0)
        
        return result
        