import codewars_test as test


# def solution(args):
#     start = args[0]
#     end = start
#     ret = str(start)

#     for i in args[1:]:
#         if i - end == 1:
#             end += 1
#         else:
#             if end - start > 1:
#                 ret += "-"
#                 ret += str(end)
#             elif end - start > 0:
#                 if ret:
#                     ret += ","
#                 ret += str(end)
#             ret += ","
#             ret += str(i)
#             start = i
#             end = i

#     if end - start > 1:
#         ret += "-"
#         ret += str(end)
#     elif end - start > 0:
#         if ret:
#             ret += ","
#             ret += str(end)
#     return ret


def solution(args):
    start = end = args[0]
    res = []

    for num in args[1:] + [0]:
        if num != end + 1:
            if start == end:
                res.append(f"{start}")
            elif start + 1 == end:
                res.append(f"{start}")
                res.append(f"{end}")
            else:
                res.append(f"{start}-{end}")
            start = num
        end = num
    return ",".join(res)


@test.describe("Range extraction")
def desc1():

    @test.it("Sample Tests")
    def it1():
        test.assert_equals(
            solution(
                [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
            ),
            "-6,-3-1,3-5,7-11,14,15,17-20",
        )
        test.assert_equals(
            solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]), "-3--1,2,10,15,16,18-20"
        )

        test.assert_equals(
            solution(
                [
                    -93,
                    -90,
                    -87,
                    -86,
                    -85,
                    -83,
                    -81,
                    -80,
                    -77,
                    -74,
                    -72,
                    -70,
                    -68,
                    -67,
                    -64,
                    -61,
                    -58,
                    -56,
                    -55,
                    -52,
                    -49,
                    -47,
                    -46,
                ]
            ),
            "-93,-90,-87--85,-83,-81,-80,-77,-74,-72,-70,-68,-67,-64,-61,-58,-56,-55,-52,-49,-47,-46",
        )
