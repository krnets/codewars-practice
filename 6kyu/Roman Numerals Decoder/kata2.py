def solution(roman: str) -> int:
    d = dict( M=1000, CM=900, D=500, CD=400, C=100, XC=90, L=50, XL=40, X=10, IX=9, V=5, IV=4, I=1,)
    ans = 0
    i = 0
    while i < len(roman):
        if (r := roman[i : i + 2]) in d:
            ans += d[r]
            i += 2
        else:
            ans += d.get(roman[i], 0)
            i += 1
    return ans


import codewars_test as test


@test.describe("Tests")
def tests():

    def do_test(roman: str, n: int):
        actual = solution(roman)
        test.assert_equals(actual, n, f"for roman {roman}")

    @test.it("Sample Tests")
    def sample_tests():
        do_test("MMMCMXCIX", 3999)
        do_test("MMMDCCCLXXXVIII", 3888)
        do_test("MM", 2000)
        do_test("MDCLXVI", 1666)
        do_test("M", 1000)
        do_test("CD", 400)
        do_test("XC", 90)
        do_test("XL", 40)
        do_test("I", 1)
