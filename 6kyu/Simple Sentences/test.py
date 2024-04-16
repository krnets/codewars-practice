import codewars_test as test
from kata import make_sentences

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(make_sentences(['hello', 'world']), 'hello world.')
    test.assert_equals(make_sentences(['Quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']), 'Quick brown fox jumped over the lazy dog.')
    
    test.assert_equals(make_sentences(['hello', ',', 'my', 'dear']), 'hello, my dear.')
    test.assert_equals(make_sentences(['one', ',', 'two', ',', 'three']), 'one, two, three.')
    test.assert_equals(make_sentences(['One', ',', 'two', 'two', ',', 'three', 'three', 'three', ',', '4', '4', '4', '4']), 'One, two two, three three three, 4 4 4 4.')
    
    test.assert_equals(make_sentences(['hello', 'world', '.']), 'hello world.')
    test.assert_equals(make_sentences(['Bye', '.']), 'Bye.')
    
    test.assert_equals(make_sentences(['hello', 'world', '.', '.', '.']), 'hello world.')
    test.assert_equals(make_sentences(['The', 'Earth', 'rotates', 'around', 'The', 'Sun', 'in', '365', 'days', ',', 'I', 'know', 'that', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']), 'The Earth rotates around The Sun in 365 days, I know that.')
