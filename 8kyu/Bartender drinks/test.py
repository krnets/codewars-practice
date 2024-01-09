from random import random, randrange, choice
from string import ascii_letters
from kata import get_drink_by_profession
import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():

    @test.it("Mixed case 1")
    def mixed_case_1():
        test.assert_equals(get_drink_by_profession(
            "jabrOni"), "Patron Tequila", "'Jabroni' should map to 'Patron Tequila'")
        test.assert_equals(get_drink_by_profession("scHOOl counselor"), "Anything with Alcohol",
                           "'School Counselor' should map to 'Anything with alcohol'")
        test.assert_equals(get_drink_by_profession(
            "prOgramMer"), "Hipster Craft Beer", "'Programmer' should map to 'Hipster Craft Beer'")
        test.assert_equals(get_drink_by_profession(
            "bike ganG member"), "Moonshine", "'Bike Gang Member' should map to 'Moonshine'")
        test.assert_equals(get_drink_by_profession(
            "poLiTiCian"), "Your tax dollars", "'Politician' should map to 'Your tax dollars'")
        test.assert_equals(get_drink_by_profession("rapper"),
                           "Cristal", "'Rapper' should map to 'Cristal'")
        test.assert_equals(get_drink_by_profession("pundit"),
                           "Beer", "'Pundit' should map to 'Beer'")
        test.assert_equals(get_drink_by_profession(
            "Pug"), "Beer", "'Pug' should map to 'Beer'")

    @test.it("Mixed case 2")
    def mixed_case_2():
        test.assert_equals(get_drink_by_profession(
            "jabrOnI"), "Patron Tequila", "'Jabroni' should map to 'Patron Tequila'")
        test.assert_equals(get_drink_by_profession("scHOOl COUnselor"), "Anything with Alcohol",
                           "'School Counselor' should map to 'Anything with alcohol'")
        test.assert_equals(get_drink_by_profession(
            "prOgramMeR"), "Hipster Craft Beer", "'Programmer' should map to 'Hipster Craft Beer'")
        test.assert_equals(get_drink_by_profession(
            "bike GanG member"), "Moonshine", "'Bike Gang Member' should map to 'Moonshine'")
        test.assert_equals(get_drink_by_profession(
            "poLiTiCiAN"), "Your tax dollars", "'Politician' should map to 'Your tax dollars'")
        test.assert_equals(get_drink_by_profession("RAPPer"),
                           "Cristal", "'Rapper' should map to 'Cristal'")
        test.assert_equals(get_drink_by_profession("punDIT"),
                           "Beer", "'Pundit' should map to 'Beer'")
        test.assert_equals(get_drink_by_profession(
            "pUg"), "Beer", "'Pug' should map to 'Beer'")


@test.describe('Random Tests')
def random_tests():
    def reference_sol(param):
        param = param.lower()
        if param == "jabroni":
            return "Patron Tequila"
        if param == "school counselor":
            return "Anything with Alcohol"
        if param == "programmer":
            return "Hipster Craft Beer"
        if param == "bike gang member":
            return "Moonshine"
        if param == "politician":
            return "Your tax dollars"
        if param == "rapper":
            return "Cristal"
        return "Beer"

    def generate_random_string():
        return ''.join([choice(ascii_letters).upper() if random() < 0.5 else choice(ascii_letters).lower() for i in range(randrange(6, 19))])

    professions = ['jabroni', 'school counselor', 'programmer',
                   'bike gang member', 'politician', 'rapper']

    def test_prof(prof):
        actual = get_drink_by_profession(prof)
        expected = reference_sol(prof)
        test.assert_equals(actual, expected)

    @test.it('Random Test Cases')
    def random_test_cases():
        for _ in range(40):
            if random() < 0.5:
                prof = ''.join([c.upper() if random() < 0.5 else c.lower()
                               for c in choice(professions)])
            else:
                prof = generate_random_string()
            test_prof(prof)
