import codewars_test as test


# def dir_reduc(arr):
#     stack = []
#     dirs = ["NORTH", "WEST", "SOUTH", "EAST"]
#     opposites = {dir: dirs[(i + 2) % len(dirs)] for i, dir in enumerate(dirs)}


#     for dir in arr:
#         if stack and dir == opposites.get(stack[-1], ""):
#             stack.pop()
#         else:
#             stack.append(dir)
#     return stack


def dir_reduc(arr):
    stack = []
    dirs = ["NORTH", "WEST", "SOUTH", "EAST"]
    opposites = {dir: dirs[(i + 2) % len(dirs)] for i, dir in enumerate(dirs)}

    for dir in arr:
        if stack and stack[-1] == opposites[dir]:
            stack.pop()
        else:
            stack.append(dir)
    return stack

    # return res


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
        test.assert_equals(dir_reduc(a), ["WEST"])
        a = ["NORTH", "WEST", "SOUTH", "EAST"]
        test.assert_equals(dir_reduc(a), ["NORTH", "WEST", "SOUTH", "EAST"])
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]  # ['WEST']
        test.assert_equals(dir_reduc(a), ["WEST"])
        a = [
            "NORTH",
            "SOUTH",
            "EAST",
            "WEST",
            "NORTH",
            "NORTH",
            "SOUTH",
            "NORTH",
            "WEST",
            "EAST",
        ]  # ['NORTH', 'NORTH']
        test.assert_equals(dir_reduc(a), ["NORTH", "NORTH"])
        a = []  # []
        test.assert_equals(dir_reduc(a), [])
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]  # []
        test.assert_equals(dir_reduc(a), [])
        a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "NORTH"]  # ["NORTH"]
        test.assert_equals(dir_reduc(a), ["NORTH"])
        a = [
            "EAST",
            "EAST",
            "WEST",
            "NORTH",
            "WEST",
            "EAST",
            "EAST",
            "SOUTH",
            "NORTH",
            "WEST",
        ]  # ["EAST", "NORTH"]
        test.assert_equals(dir_reduc(a), ["EAST", "NORTH"])
        a = [
            "NORTH",
            "EAST",
            "NORTH",
            "EAST",
            "WEST",
            "WEST",
            "EAST",
            "EAST",
            "WEST",
            "SOUTH",
        ]  # ["NORTH", "EAST"])
        test.assert_equals(dir_reduc(a), ["NORTH", "EAST"])
        a = ["NORTH", "WEST", "SOUTH", "EAST"]  # ["NORTH", "WEST", "SOUTH", "EAST"])
        test.assert_equals(dir_reduc(a), ["NORTH", "WEST", "SOUTH", "EAST"])
        a = [
            "NORTH",
            "NORTH",
            "EAST",
            "SOUTH",
            "EAST",
            "EAST",
            "SOUTH",
            "SOUTH",
            "SOUTH",
            "NORTH",
        ]
        test.assert_equals(
            dir_reduc(a),
            ["NORTH", "NORTH", "EAST", "SOUTH", "EAST", "EAST", "SOUTH", "SOUTH"],
        )
