import codewars_test as test
from kata import task


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            task("Wednesday", 10, 2),
            "It is Wednesday today, Robert, you have to work, you must spray 10 trees and you need 20 dollars to buy liquid",
        )
        test.assert_equals(
            task("Monday", 4, 3),
            "It is Monday today, James, you have to work, you must spray 4 trees and you need 12 dollars to buy liquid",
        )
        test.assert_equals(
            task("Friday", 5, 4),
            "It is Friday today, William, you have to work, you must spray 5 trees and you need 20 dollars to buy liquid",
        )
        test.assert_equals(
            task("Tuesday", 6, 1),
            "It is Tuesday today, John, you have to work, you must spray 6 trees and you need 6 dollars to buy liquid",
        )
        test.assert_equals(
            task("Thursday", 5, 3),
            "It is Thursday today, Michael, you have to work, you must spray 5 trees and you need 15 dollars to buy liquid",
        )
