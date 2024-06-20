# array_packing = lambda arr: arr[0] if len(arr) == 1 else int("".join(f"{x:08b}" for x in reversed(arr)), 2)


# def array_packing(arr):
#     return int.from_bytes(arr, byteorder="little")


def array_packing(arr):
    return sum(x << (8 * i) for i, x in enumerate(arr))
