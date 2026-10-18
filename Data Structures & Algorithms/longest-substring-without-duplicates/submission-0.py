class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        seen_chars = set()
        for right, char in enumerate(s):
            while char in seen_chars:
                seen_chars.remove(s[left])
                left += 1

            curr_len = right - left + 1
            max_len = max(max_len, curr_len)
            seen_chars.add(char)
        
        return max_len
        