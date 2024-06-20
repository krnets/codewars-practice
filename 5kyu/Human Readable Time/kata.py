import codewars_test as test


# def make_readable(seconds):
#     hh = seconds // 60 // 60
#     mm = (seconds // 60) % 60
#     return f"{hh:02}:{mm:02}:{seconds % 60:02}"


def make_readable(seconds):
    hh, ss = divmod(seconds, 60**2)
    mm, ss = divmod(ss, 60)
    return f"{hh:02}:{mm:02}:{ss:02}"

# def make_readable(seconds):
#     return "{:02}:{:02}:{:02}".format(seconds // 60 // 60, (seconds // 60) % 60, seconds % 60)

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(make_readable(0), "00:00:00")
        test.assert_equals(make_readable(59), "00:00:59")
        test.assert_equals(make_readable(60), "00:01:00")
        test.assert_equals(make_readable(3599), "00:59:59")
        test.assert_equals(make_readable(3600), "01:00:00")
        test.assert_equals(make_readable(86399), "23:59:59")
        test.assert_equals(make_readable(86400), "24:00:00")
        test.assert_equals(make_readable(359999), "99:59:59")