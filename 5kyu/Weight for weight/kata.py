import codewars_test as test


# def order_weight(strng):
#     weighted = sorted((sum(map(int, num)), num) for num in strng.split())
#     return " ".join(num for weight, num in weighted)


# def order_weight(strng):
#     return " ".join(sorted(sorted(strng.split()), key=lambda x: sum(map(int, x))))

# def order_weight(strng):
#     return " ".join( sorted(strng.split(), key=lambda x: (sum(int(d) for d in x) , x)  ) )


def order_weight(strng):
    return " ".join(sorted(strng.split(), key=lambda x: (sum(map(int, x)), x)))


@test.describe("Weight for weight")
def tests():
    @test.it("basic tests")
    def basics1():
        test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
        test.assert_equals(
            order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"),
            "11 11 2000 10003 22 123 1234000 44444444 9999",
        )
        test.assert_equals(order_weight(""), "")
