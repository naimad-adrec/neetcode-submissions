class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []

        unseen_nums = set(nums)
        
        def backtrack():
            if not unseen_nums:
                result.append(perm.copy())
                return
            
            for num in list(unseen_nums):
                unseen_nums.remove(num)
                perm.append(num)
                backtrack()
                perm.pop()
                unseen_nums.add(num)

            return
        
        backtrack()

        return result
        