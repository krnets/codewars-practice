import codewars_test as test
from kata import sexy_name

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Not too sexy!')
    def nts():
        test.assert_equals(sexy_name('GUV'), 'NOT TOO SEXY')
        test.assert_equals(sexy_name('PHUG'),"NOT TOO SEXY")
        test.assert_equals(sexy_name('FFFFF'), 'NOT TOO SEXY')
        test.assert_equals(sexy_name(''),"NOT TOO SEXY")
        test.assert_equals(sexy_name('PHUG'),"NOT TOO SEXY")

    @test.it('Pretty sexy!')
    def ps():
        test.assert_equals(sexy_name('BOB'),"PRETTY SEXY")
        test.assert_equals(sexy_name('JLJ'), 'PRETTY SEXY')
        test.assert_equals(sexy_name('HHHHHU'), 'PRETTY SEXY')
        test.assert_equals(sexy_name('BOB'),"PRETTY SEXY")
        test.assert_equals(sexy_name('WWWWWU'),"PRETTY SEXY")

    @test.it('Very sexy!')
    def vs():
        test.assert_equals(sexy_name('YOU'), 'VERY SEXY')
        test.assert_equals(sexy_name('FABIO'),"VERY SEXY")
        test.assert_equals(sexy_name('ARUUUUUUUUU'), 'VERY SEXY')

    @test.it('The ultimate sexiest!')
    def tus():
        test.assert_equals(sexy_name('ROBBY'), 'THE ULTIMATE SEXIEST')
        test.assert_equals(sexy_name('SAMANTHA'), 'THE ULTIMATE SEXIEST')
        test.assert_equals(sexy_name('DONALD TRUMP'), "THE ULTIMATE SEXIEST")
        test.assert_equals(sexy_name('BILL GATES'), "THE ULTIMATE SEXIEST")
        test.assert_equals(sexy_name('SCARLETT JOHANSSON'), "THE ULTIMATE SEXIEST")
        test.assert_equals(sexy_name('CODEWARS'),"THE ULTIMATE SEXIEST")
        test.assert_equals(sexy_name('PAMELA ANDERSON'),"THE ULTIMATE SEXIEST")

    @test.it('Should also handle lowercase letters')
    def low():
        test.assert_equals(sexy_name('you'), 'VERY SEXY')
        test.assert_equals(sexy_name('Codewars'),"THE ULTIMATE SEXIEST")