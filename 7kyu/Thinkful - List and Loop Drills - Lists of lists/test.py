from kata import process_data
import codewars_test as test


@test.describe("Lists of lists")
def lists_of_lists():

    @test.it("Examples")
    def examples():
        test.assert_equals(process_data([[2, 5], [3, 4], [8, 7]]), 3)
        test.assert_equals(process_data([[2, 9], [2, 4], [7, 5]]), 28)
