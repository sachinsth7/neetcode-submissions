class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix = 1
        suffix = 1
        result = [1] * size
        for i in range(size):
            result[i] = prefix
            prefix *= nums[i]
        for i in range(size-1, -1, -1):
            result[i] = result[i] * suffix
            suffix *= nums[i]
        return result