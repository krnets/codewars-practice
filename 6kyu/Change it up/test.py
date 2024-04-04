import codewars_test as test
from kata import changer

@test.describe('Changer tests...')
def _():

    @test.it("Basic tests")
    def _():
        test.assert_equals(changer('Cat30'), 'dbU30')
        test.assert_equals(changer('Alice'), 'bmjdf')
        test.assert_equals(changer('sponge1'), 'tqpOhf1')
        test.assert_equals(changer('Hello World'), 'Ifmmp xpsmE')
        test.assert_equals(changer('dogs'), 'Epht')
        test.assert_equals(changer('z'), 'A')
        test.assert_equals(changer('IZxzfNIYjBbgS7B2R1Jk'), 'jAyAgOjzkccht7c2s1kl')
        test.assert_equals(changer('S c HAn VhCRuz4ZdhCbBdyl3V ipuuKv'), 't d IbO wIdsvA4AEIdccEzm3w jqvvlw')
        test.assert_equals(changer('elNitjwLBY1ufAELnipuqB9S'), 'fmOjUkxmcz1vgbfmOjqvrc9t')
        test.assert_equals(changer(' CNYv7EIwAb'), ' dOzw7fjxbc')