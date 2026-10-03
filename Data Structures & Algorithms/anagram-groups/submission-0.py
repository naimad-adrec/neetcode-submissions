class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_to_strs = defaultdict(list)

        for string in strs:
            freq = [0] * 26

            for char in string:
                freq[ord(char) - ord('a')] += 1
            
            freq_to_strs[tuple(freq)].append(string)
        
        return list(freq_to_strs.values())
        