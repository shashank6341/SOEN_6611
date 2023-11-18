class Statistics:

    def __init__(self):
        self.data = []

    def read_data(self, data):
        quicksort(data,0,len(data)-1)
        self.data = data
        
    def min(self):
        return self.data[0]
    
    def max(self):
        return self.data[-1]

    def mode(self):
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
    
    def median(self):
        n = len(self.data)
        
        if n % 2 == 0:
            median1 = self.data[n//2]
            median2 = self.data[n//2 - 1]
            return (median1 + median2) / 2
        else:
            return self.data[n//2]

    def mean(self):
        total = 0
        for x in self.data:
            total += x
        return total / len(self.data)

    def mad(self):
        mean = self.mean()
        total = 0
        for x in self.data:
            total += abs(x - mean)
        return total / len(self.data)

    def stdev(self):
        return self.sqrt(self.variance())
    
    def sqrt(self,x):
        if x < 0:
            return None
        if x == 0:
            return 0
        guess = x / 2
        while abs(guess * guess - x) > 1e-12:
            guess = (guess + x / guess) / 2
        return guess


    def variance(self):
        mean = self.mean()
        total = 0
        for x in self.data:
            total += (x - mean)**2
        return total / (len(self.data) - 1)
    
def partition(arr, start, end):
    pivot = arr[end]
    pivot_index = start - 1
    for index in range(start, end):
        if arr[index] <= pivot:
            pivot_index = pivot_index + 1
            tmp = arr[pivot_index]
            arr[pivot_index] = arr[index]
            arr[index] = tmp
    tmp = arr[pivot_index + 1]
    arr[pivot_index + 1] = arr[end]
    arr[end] = tmp
    return pivot_index + 1
 
def quicksort(arr, start, end):
    if start < end:
        pivot_position = partition(arr, start, end)
        quicksort(arr, start, pivot_position - 1)
        quicksort(arr, pivot_position + 1, end)    