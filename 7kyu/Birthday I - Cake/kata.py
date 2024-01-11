from string import ascii_lowercase as abc

def cake(candles, debris):
    threshold = 0.7
    fallen_total = sum(abc.index(c) if i % 2 else ord(c) for i, c in enumerate(debris))
    return "Fire!" if candles and fallen_total > candles * threshold else "That was close!"
