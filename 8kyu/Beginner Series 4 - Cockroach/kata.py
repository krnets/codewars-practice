import codewars_test as test


# def cockroach_speed(km_per_hour):
#     cm_per_second = km_per_hour / 0.036
#     return int(cm_per_second)


def cockroach_speed(km_per_hour):
    cm_in_km = 10e4
    seconds_in_hour = 60**2
    cm_per_second = km_per_hour * (cm_in_km / seconds_in_hour)
    return int(cm_per_second)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(cockroach_speed(1.08), 30)
        test.assert_equals(cockroach_speed(1.09), 30)
        test.assert_equals(cockroach_speed(0), 0)
