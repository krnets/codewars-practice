import codewars_test as test
from kata import get_participants

@test.describe('Fixed tests')
def _():
    @test.it('0 handshakes')
    def _(): test.assert_equals(get_participants(0), 0)
    
    @test.it('1 handshake')
    def _(): test.assert_equals(get_participants(1), 2)
    
    @test.it('3 handshakes')
    def _(): test.assert_equals(get_participants(3), 3)
    
    @test.it('6 handshakes')
    def _(): test.assert_equals(get_participants(6), 4)
    
    @test.it('7 handshakes')
    def _(): test.assert_equals(get_participants(7), 5)