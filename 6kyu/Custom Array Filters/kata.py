class list:
    def __init__(self, arr) -> None:
        self.arr = [v for v in arr if type(v) is int]

    def even(self):
        return [v for v in self.arr if v % 2 == 0]

    def odd(self):
        return [v for v in self.arr if v & 1]

    def under(self, threshold):
        return [v for v in self.arr if v < threshold]

    def over(self, threshold):
        return [v for v in self.arr if v > threshold]

    def in_range(self, start, end):
        return [v for v in self.arr if start <= v <= end]
