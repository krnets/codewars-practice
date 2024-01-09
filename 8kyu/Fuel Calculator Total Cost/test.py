from kata import fuel_price
import codewars_test as test

test.assert_equals(fuel_price(10, 21.5), 212.5)
test.assert_equals(fuel_price(40, 10), 390)
test.assert_equals(fuel_price(15, 5.83), 83.7)


@test.describe("Fixed tests")
def fixed_tests():
    test.assert_equals(fuel_price(10, 21.5), 212.5)
    test.assert_equals(fuel_price(40, 10), 390)
    test.assert_equals(fuel_price(15, 5.83), 83.7)


@test.describe("Random tests")
def random_tests():
    from random import randint

    def solution(litres, price_per_liter):
        discount = min(litres // 2 * 5, 25) * 0.01
        return round(litres * (price_per_liter - discount), 2)

    for _ in range(100):
        amount, price = randint(1, 200), randint(6, 35)
        test.assert_equals(fuel_price(amount, price), solution(amount, price))
