class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = defaultdict()
        for i,n in enumerate(nums):
            leftout = target - n
            if leftout in lookup:
                return [lookup.get(leftout), i]
            lookup[n] = i
        return False
                        
            