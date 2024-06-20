import codewars_test as test


def converter(mpg):
    litres_in_gallon = 4.54609188
    km_in_mile = 1.609344
    ans = mpg * km_in_mile / litres_in_gallon
    return round(ans, 2)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(converter(10), 3.54)
        test.assert_equals(converter(20), 7.08)
        test.assert_equals(converter(30), 10.62)
        test.assert_equals(converter(24), 8.50)
        test.assert_equals(converter(36), 12.74)
