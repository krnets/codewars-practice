import codewars_test as test
from kata import reverse

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse('Hello World'), 'World Hello')
        test.assert_equals(reverse('Hi There.'), 'There. Hi')
        test.assert_equals(reverse('I am an expert at this'), 'this at expert an am I')
        test.assert_equals(reverse('This is so easy'), 'easy so is This')
        test.assert_equals(reverse('no one cares'), 'cares one no')

@test.describe('Random Tests')
def random_test():    
    import random
    
    def r(st):
        return ' '.join(reversed(st.split()))
    
    c = 'qwertyuiopasdfghjkl '
    
    for _ in range(0, 9):
        d = "".join(random.choice(c) for y in range(random.randint(0, 100)))
        @test.it(f"testing for reverse({d})")
        def test_case():
            test.assert_equals(reverse(d), r(d))