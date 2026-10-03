class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bag = set()
        for number in nums:
            if number in bag:
                return True
            bag.add(number)
        return False 