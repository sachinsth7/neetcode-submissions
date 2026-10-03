class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_character = set()
        left = 0
        longest = 0
        for right in range(len(s)):
            while s[right] in seen_character:
                seen_character.remove(s[left])
                left +=1
            seen_character.add(s[right])
            longest = max(longest, len(seen_character))
        return longest