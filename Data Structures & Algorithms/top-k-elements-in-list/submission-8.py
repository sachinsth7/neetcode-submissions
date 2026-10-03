class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = [[] for _ in range(len(nums)+ 1)]
        counted_dict = Counter(nums)
        for value, count in counted_dict.items():
            sorted_nums[count].append(value)
        result = []
        for i in range(len(sorted_nums) - 1, 0, -1):
            for v in sorted_nums[i]:
                result.append(v)
                if len(result) == k:
                    return result

            