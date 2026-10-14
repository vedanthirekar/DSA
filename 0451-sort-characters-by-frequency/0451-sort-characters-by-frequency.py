class Solution:
    def frequencySort(self, s: str) -> str:
        # counter = Counter(s)
        counter = {}
        for char in s:
            if char in counter:
                counter[char]+=1
            else:
                counter[char] =1

        freq_list = []
        for key, value in counter.items():
            freq_list.append((-value,key))

        heapq.heapify(freq_list)

        res = ""
        while freq_list:
            freq, char = heapq.heappop(freq_list)
            res += char*abs(freq)

        return res