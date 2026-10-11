class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0 
        max_character = 0
        for right in range(len(s)):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(s[right])
            max_character = max(max_character, len(seen))
        return max_character