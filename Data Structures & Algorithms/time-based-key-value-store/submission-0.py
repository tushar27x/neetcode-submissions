class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        result = ""
        arr = self.store[key]

        l = 0
        h = len(arr) - 1

        while l<=h:
            m = l + (h-l) // 2
            if arr[m][0] <= timestamp:
                result = arr[m][1]
                l = m+1
            else:
                h = m-1
        
        return result