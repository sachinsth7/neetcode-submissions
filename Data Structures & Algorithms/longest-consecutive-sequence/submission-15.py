class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsets = set(nums)
        longest = 0
        for num in numsets:
            if num-1 in numsets:
                continue
            consecutive = 1
            while num+1 in numsets:
                consecutive += 1
                num += 1
            longest = max(longest, consecutive)
        return longest
