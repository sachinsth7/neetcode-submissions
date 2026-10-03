class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_sorted = [[] for _ in range(len(nums)+1)]
        count = Counter(nums)
        result = []
        for value, freq in count.items():
            counted_sorted[freq].append(value)
        for i in range(len(counted_sorted)-1, -1, -1):
            for value in counted_sorted[i]:
                result.append(value)
                if len(result) == k:
                    return result