class TimeMap:

    def __init__(self):

        self.values = defaultdict(list)
        self.times = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.values[key].append(value)
        self.times[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:

        times = self.times[key]
        values = self.values[key]
        l = 0
        r = len(times)-1

        while l <= r:

            m = (l + r) // 2
            if times[m] == timestamp:
                return values[m]
            if times[m] > timestamp:
                r = m - 1
            else:
                l = m + 1
        
        return values[l-1] if (l-1 < len(values) and l-1 >= 0) else ""
            
        
