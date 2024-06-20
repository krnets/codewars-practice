from operator import itemgetter
import codewars_test as test


# def order(sentence):
#     words = sentence.split()
#     positions = []

#     for word in words:
#         for c in word:
#             if c.isdigit():
#                 positions.append((int(c) - 1, word))
#                 break

#     return " ".join(map(itemgetter(1), sorted(positions, key=itemgetter(0))))


def order(sentence):
    return " ".join(sorted(sentence.split(), key=min))


@test.describe("Your order, please")
def desc1():
    @test.it("Sample tests")
    def it1():
        test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
        test.assert_equals(
            order("4of Fo1r pe6ople g3ood th5e the2"),
            "Fo1r the2 g3ood 4of th5e pe6ople",
        )
        test.assert_equals(order(""), "")
