class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_dict = {}
        for i, value in enumerate(nums):
            needed = target - value
            if needed in lookup_dict:
                seen = lookup_dict.get(needed)
                return [seen, i]
            lookup_dict[value] = i