from collections import Counter

class TempTracker:
    def __init__(self):
        self.max = 0
        self.min = 110
        self.mean = 0
        self.recorded_temperatures = Counter()
        self.sum_temperatures = 0
        self.n_records = 0

    def insert(self, temperature):
        if temperature > self.max:
            self.max = temperature
        if temperature < self.min:
            self.min = temperature
        self.sum_temperatures += temperature
        self.n_records += 1
        self.mean = self.sum_temperatures / self.n_records
        self.recorded_temperatures[temperature] += 1

    def get_max(self):
        return self.max if self.n_records else None

    def get_min(self):
        return self.min if self.n_records else None

    def get_mean(self):
        return self.mean if self.n_records else None


    def get_mode(self):
        return self.recorded_temperatures.most_common()[0][0] if self.recorded_temperatures else None