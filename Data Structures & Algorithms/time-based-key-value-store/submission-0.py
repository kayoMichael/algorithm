import bisect
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.store[key], (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.store[key])
        lst = self.store[key]
        while left < right:
            mid = (right + left) // 2

            if lst[mid][0] <= timestamp:
                left = mid + 1

            else:
                right = mid

        return self.store[key][left - 1][1] if left > 0 else ""