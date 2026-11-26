class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        mood = self.storage.get(key, [])
        left = 0
        right = len(mood) - 1
        result = ''
        while left <= right:
            mid = (left + right) // 2
            if mood[mid][0] <= timestamp:
                result = mood[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result 
