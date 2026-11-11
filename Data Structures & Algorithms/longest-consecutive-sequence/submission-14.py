class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsets = set(nums)
        longest = 0
        for num in numsets:
            if num - 1 in numsets:
                continue
            consecutive = 1
            while num + 1 in numsets:
                num += 1
                consecutive += 1
            longest = max(consecutive, longest)
        return longest