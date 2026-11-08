class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = Counter(s)
        s2 = Counter(t)
        return s1 == s2