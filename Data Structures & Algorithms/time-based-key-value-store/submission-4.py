class TimeMap:

    def __init__(self):
        self.profile = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.profile:
            self.profile[key] = []
        self.profile[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.profile:
            return ""
        values = self.profile.get(key)
        left = 0
        right = len(values) - 1
        result = ''
        while left <= right:
            mid = (left+right) // 2
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result
