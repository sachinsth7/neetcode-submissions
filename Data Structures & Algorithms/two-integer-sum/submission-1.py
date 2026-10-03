class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            compliment = target - x
            if compliment in seen:
                return [seen[compliment], i]
            seen[x] = i
            
            