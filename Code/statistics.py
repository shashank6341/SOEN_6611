class Statistics:

    def __init__(self):
        self.data = []

    def read_data(self, data):
        self.data = sorted(data)
        
    def get_min(self):
        return self.data[0]
    
    def get_max(self):
        return self.data[-1]

    def get_mode(self):
        freq = {}
        for x in self.data:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1
        
        max_freq = 0
        modes = []
        for x, f in freq.items():
            if f > max_freq:
                max_freq = f
                modes = [x]
            elif f == max_freq:
                modes.append(x)
        
        return modes
    
    def get_median(self):
        n = len(self.data)
        
        if n % 2 == 0:
            median1 = self.data[n//2]
            median2 = self.data[n//2 - 1]
            return (median1 + median2) / 2
        else:
            return self.data[n//2]

    def get_mean(self):
        total = 0
        for x in self.data:
            total += x
        return total / len(self.data)

    def get_mad(self):
        mean = self.get_mean()
        total = 0
        for x in self.data:
            total += abs(x - mean)
        return total / len(self.data)

    def get_stdev(self):
        return self.sqrt(self.get_variance())

    def get_variance(self):
        mean = self.get_mean()
        total = 0
        for x in self.data:
            total += (x - mean)**2
        return total / (len(self.data) - 1)