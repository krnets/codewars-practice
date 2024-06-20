def max_ball(v0):
    gravity = 9.81  #  m/s**2
    speed = v0 / 3.6  # convert km/h to m/s - international system of units
    heights, max_height, time = [], 0, 0
    calc_height = lambda v, t: v * t - 0.5 * gravity * t * t

    while (height := calc_height(speed, time)) >= 0:
        heights.append(height)
        time += 0.1

        if heights[-1] > max_height:
            max_height = heights[-1]
            time_in_tenth_of_second = len(heights)

    return time_in_tenth_of_second - 1
