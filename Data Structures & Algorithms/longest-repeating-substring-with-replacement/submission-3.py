class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        chars = set(s)
        max_len = 0
        for char in chars:
            char_count = left = 0
            for right in range(n):
                if s[right] == char:
                    char_count += 1

                while (right - left + 1) - char_count > k:
                    if s[left] == char:
                        char_count -= 1
                    left += 1
                
                max_len = max(max_len, right - left + 1)

        return max_len
        