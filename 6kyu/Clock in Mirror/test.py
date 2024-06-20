from kata import what_is_the_time
import codewars_test as test

@test.describe("Testing...")
def _():
    
    @test.it("Fixed tests")
    def _():
        test.assert_equals(what_is_the_time("06:35"), "05:25", "Didn't work for '06:35'")
        test.assert_equals(what_is_the_time("11:59"), "12:01", "Didn't work for '11:59'")
        test.assert_equals(what_is_the_time("12:02"), "11:58", "Didn't work for '12:02'")
        test.assert_equals(what_is_the_time("04:00"), "08:00", "Didn't work for '04:00'")
        test.assert_equals(what_is_the_time("06:00"), "06:00", "Didn't work for '06:00'")
        test.assert_equals(what_is_the_time("12:00"), "12:00", "Didn't work for '12:00'")


    @test.it("Returns the original time when applied twice to a time")
    def _():

        for time in ("06:35", "11:59", "12:02", "04:00", "06:00", "12:00"):
            test.assert_equals(what_is_the_time(what_is_the_time(time)), time, "didn't work for "+ time)
