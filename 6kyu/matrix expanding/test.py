import codewars_test as test
from kata import expand


def tester(m, fill, soln):
    user = expand(m, fill)
    if len(user) != len(soln) or len(user[0]) != len(soln):
        print("your dimensions didn't match")
        return False
    for i, row in enumerate(user):
        for j, ele in enumerate(row):
            if ele != soln[i][j]:
                print("---FAILED---")
                print_mat(m)
                print("produced")
                print_mat(user)
                print("I wanted")
                print_mat(soln)
                print("------------")
                return False
    return True


mat = [[1, 1], [1, 1]]
correct_mat = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
test.expect(tester(mat, 0, correct_mat))
