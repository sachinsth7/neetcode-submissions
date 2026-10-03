class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counted_dict = Counter(nums)
        for value, count in counted_dict.items():
            heapq.heappush(heap, (count, value))
            if len(heap) > k:
                heapq.heappop(heap)
        return [value for freq, value in heap]
            