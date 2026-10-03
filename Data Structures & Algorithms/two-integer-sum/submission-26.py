class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_check = defaultdict()
        for index, num in enumerate(nums):
            needed = target - num
            if needed in result_check:
                j = result_check[needed]
                return [j, index]
            result_check[num] = index
        