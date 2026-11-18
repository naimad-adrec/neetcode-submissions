class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        combination = []

        def backtracking(i, curr_sum):
            if curr_sum >= target or i >= len(candidates):
                if curr_sum == target:
                    result.append(combination.copy())
                return
            
            candidate = candidates[i]
            combination.append(candidate)
            i += 1
            backtracking(i, curr_sum + candidate)
            combination.pop()

            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1
            
            backtracking(i, curr_sum)

            return
        
        backtracking(0, 0)

        return result
        