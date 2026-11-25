class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        time_slots = self.time.get(key, [])
        left = 0
        right = len(time_slots) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            if time_slots[mid][0] <= timestamp:
                result = time_slots[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result
