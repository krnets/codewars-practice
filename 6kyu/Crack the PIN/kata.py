from hashlib import md5

# def crack(hash):
#     for i in range(int(1e5)):
#         pin_candidate = f"{i:05}"
#         encoded = md5(pin_candidate.encode()).hexdigest()
#         if encoded == hash:
#             return pin_candidate


# def crack(hash):
#     return next(pin for i in range(int(1e5)) if hash == md5((pin := f"{i:05}").encode()).hexdigest())


def crack(hash):
    return next(pin for i in range(int(1e5)) if hash == md5((pin := str(i).zfill(5)).encode()).hexdigest())
