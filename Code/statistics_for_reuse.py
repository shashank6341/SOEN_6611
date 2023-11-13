import numpy as np
import scipy.stats as stats

class Statistics:

    def __init__(self):
        self.data = []

    def read_data(self, data):
        self.data = np.array(data)
        self.data.sort()
        
    def min(self):
        return np.min(self.data)

    def max(self):
        return np.max(self.data)

# mode is broken
    def mode(self):
        return stats.mode(self.data)

    def median(self):
        return np.median(self.data)

    def mean(self):
        return np.mean(self.data)

    def mad(self):
        return np.mean(np.abs(self.data - self.mean()))

    def stdev(self):
        return np.std(self.data, ddof=1)

    def variance(self):
        return np.var(self.data, ddof=1)
