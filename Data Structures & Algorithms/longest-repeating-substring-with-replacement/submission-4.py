class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_to_freq = defaultdict(int)
        max_len = left = max_freq = 0

        for right in range(len(s)):
            char_to_freq[s[right]] += 1
            max_freq = max(max_freq, char_to_freq[s[right]])

            while (right - left + 1) - max_freq > k:
                char_to_freq[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
        