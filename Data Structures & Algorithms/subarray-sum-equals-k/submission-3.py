class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0

        prefix_sum_to_count = defaultdict(int)
        prefix_sum_to_count[0] = 1

        prefix_sum = 0
        for num in nums:
            prefix_sum += num

            diff = prefix_sum - k
            if diff in prefix_sum_to_count:
                result += prefix_sum_to_count[diff]
            
            prefix_sum_to_count[prefix_sum] += 1

        return result
        