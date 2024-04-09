def who_took_the_car_key(message):
    return "".join(chr(int(c, 2)) for c in message)
