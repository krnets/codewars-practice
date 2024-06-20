def part(arr):
    alan_related = {"Partridge", "PearTree", "Chat", "Dan", "Toblerone", "Lynn", "AlphaPapa", "Nomad" }
    n = sum(item in alan_related for item in arr)
    return ("Mine's a Pint" + "!" * n) if n else "Lynn, I've pierced my foot on a spike!!"