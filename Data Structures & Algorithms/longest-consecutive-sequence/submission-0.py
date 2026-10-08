class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_nums = set(nums)
        max_len = 0

        for num in seen_nums:
            if (num - 1) not in seen_nums:
                seq_len = 1
                while (num + seq_len) in seen_nums:
                    seq_len += 1
            
                max_len = max(max_len, seq_len)
        
        return max_len
        