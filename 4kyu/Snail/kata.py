import codewars_test as test


def snail(snail_map):
    res = []
    if not snail_map[0]:
        return res
    top, bottom = 0, len(snail_map) - 1
    left, right = top, bottom

    while top <= bottom and left <= right:
        # left to right
        for j in range(left, right + 1):
            res.append(snail_map[top][j])
        top += 1

        # top to bottom
        for i in range(top, bottom + 1):
            res.append(snail_map[i][right])
        right -= 1

        # right to left
        for j in range(right, left - 1, -1):
            res.append(snail_map[bottom][j])
        bottom -= 1

        # bottom to top
        for i in range(bottom, top - 1, -1):
            res.append(snail_map[i][left])
        left += 1

    return res


array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
test.assert_equals(snail(array), expected)


array = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test.assert_equals(snail(array), expected)
