class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        char_to_last_idx = {}
        for right, char in enumerate(s):
            if char in char_to_last_idx:
                left = max(left, char_to_last_idx[char] + 1)

            curr_len = right - left + 1
            max_len = max(max_len, curr_len)
            char_to_last_idx[char] = right
        
        return max_len
        