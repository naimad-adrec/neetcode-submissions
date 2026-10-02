class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_occurance = [0] * 26
        for char in s:
            char_occurance[ord(char) - ord('a')] += 1
        
        for char in t:
            char_occurance[ord(char) - ord('a')] -= 1

        for occurance in char_occurance:
            if occurance != 0:
                return False
        
        return True
        