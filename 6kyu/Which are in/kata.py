import codewars_test as test


# def in_array(array1, array2):
#     res = []
#     for x in set(array1):
#         for y in array2:
#             if x in y:
#                 res.append(x)
#                 break
#     return sorted(res)


def in_array(array1, array2):
    return sorted(x for x in set(array1) if any(x in y for y in array2))


@test.describe("in_array")
def tests():
    def testing(array1, array2, expect):
        actual = in_array(array1, array2)
        test.assert_equals(actual, expect)

    @test.it("Basic tests")
    def basics():
        a1 = ["live", "arp", "strong"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ["arp", "live", "strong"]
        testing(a1, a2, r)
        a1 = ["arp", "mice", "bull"]
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ["arp"]
        testing(a1, a2, r)
