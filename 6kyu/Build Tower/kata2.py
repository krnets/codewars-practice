import codewars_test as test


# def tower_builder(n_floors):
#     res = []
#     width = 2 * n_floors - 1

#     for i in range(1, n_floors + 1):
#         floor = ("*" * (2 * i - 1)).center(width)
#         res.append(floor)
#     return res


# def tower_builder(n_floors):
#     res = []
#     width = 2 * n_floors - 1

#     for i in range(1, 2 * n_floors, 2):
#         floor = ("*" * i).center(width)
#         res.append(floor)
#     return res


def tower_builder(n_floors):
    m = 2 * n_floors
    return [("*" * i).center(m - 1) for i in range(1, m, 2)]


@test.describe("Build Tower")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            tower_builder(1),
            [
                "*",
            ],
        )
        test.assert_equals(tower_builder(2), [" * ", "***"])
        test.assert_equals(tower_builder(3), ["  *  ", " *** ", "*****"])
