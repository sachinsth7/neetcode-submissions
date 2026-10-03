class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsets = set(nums)
        longest = 0
        for num in numsets:
            if num-1 in numsets:
                continue
            consecutive_count = 1
            while num+1 in numsets:
                num += 1
                consecutive_count +=1
            longest = max(consecutive_count, longest)
        return longest
