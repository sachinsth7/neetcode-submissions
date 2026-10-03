class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_sorted_index = [[] for _ in range(len(nums)+ 1)]
        counted = Counter(nums)
        result = []
        for number, freq in counted.items():
            count_sorted_index[freq].append(number)
        for i in range(len(count_sorted_index)-1, 0, -1):
            for number in count_sorted_index[i]:
                result.append(number)
                if len(result) == k:
                    return result
            