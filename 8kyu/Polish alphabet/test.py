from kata import correct_polish_letters
import codewars_test as test


@test.describe('Example Tests')
def example_tests():
    test.assert_equals(correct_polish_letters(
        "Jędrzej Błądziński"), "Jedrzej Bladzinski")
    test.assert_equals(correct_polish_letters("Lech Wałęsa"), "Lech Walesa")
    test.assert_equals(correct_polish_letters(
        "Maria Skłodowska-Curie"), "Maria Sklodowska-Curie")
