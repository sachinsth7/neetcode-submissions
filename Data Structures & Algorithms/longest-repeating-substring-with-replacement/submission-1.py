class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        freq = {}
        for right in range(len(s)):
            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1

            window_size = right - left + 1
            while window_size - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
                window_size -= 1 
            longest = max(longest, window_size)
        return longest 


        