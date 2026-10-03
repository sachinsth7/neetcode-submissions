class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsets = set(nums)
        longest = 0
        for num in numsets:
            length = 1
            if num-1 not in numsets:
                start = num
                while start+1 in numsets:
                    length += 1
                    start += 1
                longest = max(length, longest)
        return longest