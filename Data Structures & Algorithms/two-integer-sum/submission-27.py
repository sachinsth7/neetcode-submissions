class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in checker:
                return [checker[remainder], i]
            checker[nums[i]] = i
        