# def fly_by(lamps, drone):
#     path_length = len(drone) if len(drone) < len(lamps) else len(lamps)
#     return "o" * path_length + lamps[path_length:]


# def fly_by(lamps, drone):
#     path_length = min(len(lamps), len(drone))
#     return "o" * path_length + lamps[path_length:]


def fly_by(lamps, drone):
    return lamps.replace("x", "o", len(drone))
