class RecentCounter:

    def __init__(self):
        self.de = deque([])
        

    def ping(self, t: int) -> int:
        while self.de and t - self.de[0] > 3000:
            self.de.popleft()

        self.de.append(t)

        return len(self.de)

        
        




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)