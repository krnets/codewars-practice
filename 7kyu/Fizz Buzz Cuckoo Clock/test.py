import codewars_test as test
from kata import fizz_buzz_cuckoo_clock

test.describe("Basic times tests")
test.it("13:34")
test.assert_equals(fizz_buzz_cuckoo_clock("13:34"), "tick")
test.it("21:00")
test.assert_equals(
    fizz_buzz_cuckoo_clock("21:00"),
    "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo",
)
test.it("11:15")
test.assert_equals(fizz_buzz_cuckoo_clock("11:15"), "Fizz Buzz")
test.it("03:03")
test.assert_equals(fizz_buzz_cuckoo_clock("03:03"), "Fizz")
test.it("14:30")
test.assert_equals(fizz_buzz_cuckoo_clock("14:30"), "Cuckoo")
test.it("08:55")
test.assert_equals(fizz_buzz_cuckoo_clock("08:55"), "Buzz")
test.it("00:00")
test.assert_equals(
    fizz_buzz_cuckoo_clock("00:00"),
    "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo",
)
test.it("12:00")
test.assert_equals(
    fizz_buzz_cuckoo_clock("12:00"),
    "Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo Cuckoo",
)
