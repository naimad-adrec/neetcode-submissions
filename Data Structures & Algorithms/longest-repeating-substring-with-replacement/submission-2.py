class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        chars = set(s)

        max_len = 0
        for char in chars:
            curr_k = k
            left = 0
            for right in range(n):
                if curr_k and s[right] != char:
                    curr_k -= 1
                elif s[right] != char:
                    while s[left] == char:
                        left += 1
                    left += 1
                
                max_len = max(max_len, right - left + 1)

        return max_len
        