class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s, freq_t = Counter(s), Counter(t)

        for key in freq_s.keys():
            if key not in freq_t:
                return False
            if freq_s[key] != freq_t[key]:
                return False

        return True        
