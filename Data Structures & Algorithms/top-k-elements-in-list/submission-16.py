class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortednums = [[] for _ in range(len(nums) + 1)] 
        counted = Counter(nums)
        result = []
        for key, v in counted.items():
            sortednums[v].append(key)
        for i in range(len(sortednums) - 1, -1, -1):
            for v in sortednums[i]:
                result.append(v)
                if len(result) == k:
                    return result
            