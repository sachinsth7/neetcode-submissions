class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)
        frequent = [[] for i in range(len(nums) + 1)]
        freq = []
        for key, value in counted.items():
            frequent[value].append(key)
        for f in range(len(frequent)-1, 0, -1):
            for elements in frequent[f]:
                freq.append(elements)
                if len(freq) == k:
                    return freq
