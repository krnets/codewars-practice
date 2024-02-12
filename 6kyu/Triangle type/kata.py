# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle


def triangle_type(a, b, c):
    a, b, c = sorted([a, b, c])
    sum_min_middle_squares = a * a + b * b
    max_side_square = c * c

    if a + b <= c:
        return 0
    if sum_min_middle_squares > max_side_square:
        return 1
    if sum_min_middle_squares == max_side_square:
        return 2
    if sum_min_middle_squares < max_side_square:
        return 3
    return 0
