class RecentCounter:

    def __init__(self):
        self.ls = list()

    def ping(self, t: int):
        self.ls.append(t)
        for i, v in enumerate(self.ls):
            if t - 3000 <= v <= t:
                print(self.ls[i:])
                return len(self.ls[i:])


recentCounter = RecentCounter()
recentCounter.ping(1)
recentCounter.ping(100)
recentCounter.ping(3001)
recentCounter.ping(3002)
print(100 // 26)