# def mean_vs_median(numbers):
#     numbers.sort()
#     median = numbers[len(numbers) // 2]
#     mean = sum(numbers) / len(numbers)
#     return "mean" if mean > median else "median" if median > mean else "same"

from statistics import mean, median


def mean_vs_median(numbers):
    m, n = mean(numbers), median(numbers)
    return ("same", "mean", "median")[(m > n) - (m < n)]
