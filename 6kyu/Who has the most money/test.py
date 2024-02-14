import codewars_test as test
from kata import Student, most_money


@test.describe("Sample tests")
def sample_tests():

    @test.it("Examples")
    def examples():

        phil = Student("Phil", 2, 2, 1)
        cam = Student("Cameron", 2, 2, 0)
        geoff = Student("Geoff", 0, 3, 0)

        test.assert_equals(most_money([cam, geoff, phil]), "Phil")
        test.assert_equals(most_money([cam, geoff]), "all")
        test.assert_equals(most_money([geoff]), "Geoff")
