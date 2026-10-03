class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_array = set(nums)
        if len(new_array)< len(nums):
            return True
        else:
            return False