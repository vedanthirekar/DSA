class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        # res_value = ""
        if key not in self.timemap:
            return ""
        values_list = self.timemap[key]
        if values_list[0][0]>timestamp:
            return ""

        l = 0
        h = len(values_list)-1

        while l<h:
            mid = l+(h-l+1)//2
            if values_list[mid][0]<= timestamp:
                l = mid
            else:
                h = mid-1

        return values_list[l][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)