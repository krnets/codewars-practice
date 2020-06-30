""" 6kyu - Increment with iterations

Your goal in this kata is to implement an algorithm, which increases number in the way explained below, and returns the result.

Input data: number, iterations, step.

Stage 1:
We get the: number:143726, iterations: 16, step:3
And make increment operations in a special way
Position: We start from 1 position and increment 4th num, besause step is 3

s - start position
+ - current increased position

Position: s - - - - - => - - - + - -
Number:   1 4 3 7 2 6 => 1 4 3 8 2 6

Stage 2: repeat stage 1 :)

Position: - - - s - - => + - - - - -
Number:   1 4 3 8 2 6 => 2 4 3 8 2 6

You must remember: if your number overflow into a longer number, the current position gets shifted to the right

9 9 9   => - - p -   before overflow position be at 3rd digit
1 0 0 0 => - - - p - after overflow position be at 4th digit

Note:

9 => 10
799 => 800 (if you increase second 9) or 809 (if you increase first 9)
99000 => 100000 (if you increase second 9) or 109000 (if you increase first 9) """

# def increment(number, iterations, spacer):
#     pos = 0
#     for _ in range(iterations):
#         size = len(str(number))
#         pos = (pos + spacer) % size
#         number += 10**(size-pos-1)
#         if len(str(number)) > size:
#             pos += 1
#     return number

# def increment(number, iterations, spacer):
#     pos = 0
#     for _ in range(iterations):
#         size = len(str(number))
#         pos = (pos + spacer) % size
#         number += 10**(size-1-pos)
#         pos += len(str(number)) != size
#     return number

# def increment(number, iterations, spacer):
#     position = len(str(number))-1
#     for _ in range(iterations):
#         position = (position-spacer) % len(str(number))
#         number += 10**position
#     return number


def increment(number, iterations, spacer):
    pos = len(str(number))-1
    for _ in range(iterations):
        pos = (pos-spacer) % len(str(number))
        number += 10**pos
    return number


q = increment(123, 5, 2), 245
q
q = increment(14123, 15, 6), 47456
q
q = increment(9999, 9, 9), 32211
q
