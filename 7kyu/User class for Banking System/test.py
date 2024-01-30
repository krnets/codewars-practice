from kata import User
import codewars_test as test


@test.describe("User class tests")
def user_class_tests():
    @test.it("Sample Tests")
    def sample_tests():
        Jeff = User("Jeff", 70, True)
        Joe = User("Joe", 70, True)

        test.assert_equals(Jeff.withdraw(2), "Jeff has 68.")
        test.assert_equals(Joe.check(Jeff, 50), "Joe has 120 and Jeff has 18.")
        test.assert_equals(Jeff.check(Joe, 80), "Jeff has 98 and Joe has 40.")
        test.assert_equals(Jeff.add_cash(20), "Jeff has 118.")
