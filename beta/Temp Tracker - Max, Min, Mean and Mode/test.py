import codewars_test as test
from kata import TempTracker


@test.describe("Sample tests")
def _():
    def insert_temps(t, a):
        for x in a:
            t.insert(x)

    @test.it("Tests")
    def __():
        tracker = TempTracker()

        insert_temps(tracker, [5, 4, 6, 6, 8, 7])
        test.assert_equals(tracker.get_max(), 8)

        insert_temps(tracker, [4, 2, 3])
        test.assert_equals(tracker.get_min(), 2)
        test.assert_equals(tracker.get_mean(), 5)

        insert_temps(tracker, [110, 110, 110])
        test.assert_equals(tracker.get_mode(), 110)
