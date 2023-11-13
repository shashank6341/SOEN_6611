import statistics

class Statistics:

    def __init__(self):
        self.data = []

    def read_data(self, data):
        self.data = sorted(data)
        
    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def mode(self):
        return statistics.multimode(self.data)

    def median(self):
        return statistics.median(self.data)

    def mean(self):
        return statistics.mean(self.data)

    def mad(self):
        return statistics.mean([abs(x - self.mean()) for x in self.data])

    def stdev(self):
        return statistics.stdev(self.data)

    def variance(self):
        return statistics.variance(self.data)
