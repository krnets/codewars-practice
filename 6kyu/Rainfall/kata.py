import numpy as np


def mean(town: str, s: str) -> float:
    town_temperatures = get_town_temperatures(town, s)
    return np.mean(town_temperatures) if town_temperatures else -1


def variance(town: str, s: str) -> float:
    town_temperatures = get_town_temperatures(town, s)
    return np.var(town_temperatures) if town_temperatures else -1


def get_town_temperatures(town: str, s: str) -> list or None:
    for line in s.splitlines():
        city, data = line.split(":")
        if city == town:
            return [float(x.split()[-1]) for x in data.split(",")]
