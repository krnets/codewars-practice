# def alan(arr):
#     stations = [ "Rejection", "Disappointment", "Backstabbing Central", "Shattered Dreams Parkway" ]
#     return "Smell my cheese you mother!" if all(x in arr for x in stations) else "No, seriously, run. You will miss it."

def alan(arr):
    stations = { "Rejection", "Disappointment", "Backstabbing Central", "Shattered Dreams Parkway" }
    return "Smell my cheese you mother!" if stations.issubset(arr) else "No, seriously, run. You will miss it."