# Classes


class MedianFetcher:
    def __init__(self):  # Constructor  self = this
        # Define attributes
        self.median = None  # None = null and must be capitalized
        self.numbers = []
        
# Inserts the value n into our class

    def insert(self, n):
        self.numbers.append(n)
        self.numbers.sort()

# Where do we store n?
# Maybe we store it in self.median?
# What happens when we insert more values?

    def get_median(self):
        if len(self.numbers) == 1:
            return self.numbers[0]

        mid = len(self.numbers) // 2
        if len(self.numbers) % 2 == 1:
            # If it's odd
            
            return self.numbers[mid]
            
        else:
            # If it's even
            mean = ((self.numbers[mid] + self.numbers[mid -1])/2)
            return mean




def foo():
    pass   # pass is like closing the braces to signify the end of a function


medianFetcher = MedianFetcher()
medianFetcher.insert(5)
medianFetcher.insert(6)
medianFetcher.insert(7)
medianFetcher.insert(9)

print(medianFetcher.get_median())
