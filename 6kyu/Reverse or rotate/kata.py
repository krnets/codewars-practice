# def rev_rot(strng, sz):
#     if not strng or not sz or sz > len(strng):
#         return ""
#     n = len(strng)
#     chunks = [strng[i : i + sz] for i in range(0, n - n % sz, sz)]
#     return "".join(
#         chunk[::-1] if sum_cubes_digits(chunk) % 2 == 0 else chunk[1:] + chunk[0]
#         for chunk in chunks
#     )


from textwrap import wrap

def sum_digit_cubes(num_str):
    return sum(d**3 for d in map(int, num_str))

def rev_rot(strng, sz):
    if not strng or not sz or sz > len(strng):
        return ""
    m = sz * (len(strng) // sz)
    return "".join(chunk[::-1] if sum_digit_cubes(chunk) % 2 == 0 else chunk[1:] + chunk[0]
        for chunk in wrap(strng[:m], sz))
