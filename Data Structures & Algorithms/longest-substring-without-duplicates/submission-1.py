class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_character = {}
        left = 0
        longest = 0
        for right, c in enumerate(s):
            if c in seen_character and seen_character[c] >= left:
                left = seen_character[c] + 1
            seen_character[c] = right
            length = right -left +1
            longest = max(longest, length)
        return longest 
