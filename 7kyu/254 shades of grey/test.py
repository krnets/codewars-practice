import random
import codewars_test as test
from kata import shades_of_grey

@test.describe("Fixed Tests")
def _():
    @test.it("Should work for negative n")
    def _():
        test.assert_equals(shades_of_grey(-2), [])
        test.assert_equals(shades_of_grey(-1), [])
    @test.it("Should work for zero n")
    def _():
        test.assert_equals(shades_of_grey(0), [])
    @test.it("Should work for positive n")
    def _():
        test.assert_equals(shades_of_grey(1), ["#010101"])
        test.assert_equals(shades_of_grey(2), ["#010101", "#020202"])
        test.assert_equals(shades_of_grey(3), ["#010101","#020202", "#030303"])
        test.assert_equals(shades_of_grey(4), ["#010101", "#020202", "#030303", "#040404"])
        test.assert_equals(shades_of_grey(5), ["#010101", "#020202", "#030303", "#040404", "#050505"])
        test.assert_equals(shades_of_grey(6), ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606"])
        test.assert_equals(shades_of_grey(7), ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606", "#070707"])
        test.assert_equals(shades_of_grey(8), ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606", "#070707", "#080808"])
        test.assert_equals(shades_of_grey(9), ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606", "#070707", "#080808", "#090909"])
        test.assert_equals(shades_of_grey(10), ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606", "#070707", "#080808", "#090909", "#0a0a0a"])