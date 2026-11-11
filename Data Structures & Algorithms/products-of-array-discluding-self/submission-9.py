class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size
        prefix = 1
        suffix = 1
        for i in range(size):
            result[i] = prefix
            prefix *= nums[i]
        for i in range(size-1, -1, -1):  
            result[i] = result[i] * suffix
            suffix = suffix * nums[i]
        return result