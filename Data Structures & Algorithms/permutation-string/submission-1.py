class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq_counter = [0] * 26
        for char in s1:
            s1_freq_counter[ord(char) - ord('a')] += 1

        left = 0
        s2_freq_counter = [0] * 26
        for right in range(len(s2)):
            char_idx = ord(s2[right]) - ord('a')
            if s1_freq_counter[char_idx] == 0:
                s2_freq_counter = [0] * 26
                left = right + 1
                continue

            s2_freq_counter[char_idx] += 1

            while s1_freq_counter[char_idx] < s2_freq_counter[char_idx]:
                s2_freq_counter[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            if s1_freq_counter == s2_freq_counter:
                return True

        return False
        