from statistics import mean, median

# def stat(strg):
#     if not strg:
#         return strg
#     runners = sorted(to_seconds(map(int, runner.split("|"))) for runner in strg.split(", "))
#     range = runners[-1] - runners[0]
#     average = sum(runners) // len(runners)
#     n = len(runners)
#     mid = n // 2
#     median = runners[mid] if n % 2 else sum(runners[mid - 1 : mid + 1]) // 2
#     return f"Range: {from_seconds(range)} Average: {from_seconds(average)} Median: {from_seconds(median)}"


def stat(strg):
    if not strg:
        return strg
    runners = sorted(
        to_seconds(map(int, runner.split("|"))) for runner in strg.split(", ")
    )
    return f"Range: {from_seconds(runners[-1] - runners[0])} Average: {from_seconds(int(mean(runners)))} Median: {from_seconds(int(median(runners)))}"


def to_seconds(arr):
    hours, minutes, seconds = arr
    return hours * 3600 + minutes * 60 + seconds


def from_seconds(seconds):
    return f"{seconds // 3600:02}|{(seconds % 3600) // 60:02}|{seconds % 60:02}"
