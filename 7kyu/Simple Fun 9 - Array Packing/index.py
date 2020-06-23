""" 7kyu - Simple Fun #9: Array Packing
    
You are given an array of up to four non-negative integers, each less than 256.

Your task is to pack these integers into one number M in the following way:

The first element of the array occupies the first 8 bits of M;
The second element occupies next 8 bits, and so on.

Return the obtained integer M as unsigned integer.

    the phrase "first bits of M" refers to the least significant bits of M - the right-most bits of an integer. 
    For further clarification see the following example.

For a = [24, 85, 0], the output should be 21784
An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.

After packing these into one number we get 00000000 01010101 00011000 (spaces are placed for convenience), which equals to 21784.

    [input] integer array a
    Constraints: 1 ≤ a.length ≤ 4 and 0 ≤ a[i] < 256
    [output] an unsigned integer

More Challenge

    Are you a One-Liner? Please try to complete the kata in one line(no test for it) """


# def array_packing(arr):
#     return int(''.join([f'{x:b}'.zfill(8) for x in arr][::-1]), 2)

# def array_packing(arr):
#     return int.from_bytes(arr, 'little')

# def array_packing(arr):
#     return sum(x << (8 * i) for i, x in enumerate(arr))

def array_packing(arr):
    return int(''.join(f'{n:08b}' for n in reversed(arr)), 2)


q = array_packing([24, 85, 0]), 21784
q
q = array_packing([23, 45, 39]), 2567447
q
q = array_packing([1, 1]), 257
q
q = array_packing([0]), 0
q
q = array_packing([255, 255, 255, 255]), 4294967295
q
