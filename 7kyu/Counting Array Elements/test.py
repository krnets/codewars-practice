import codewars_test as test
from kata import counting_valleys

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(counting_valleys('UFFFD'), 0)
    test.assert_equals(counting_valleys('DFFFD'), 0)
    test.assert_equals(counting_valleys('UFFFU'), 0)
    test.assert_equals(counting_valleys('DFFFU'), 1)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFU'), 1)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFU'), 2)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFUUFFDDUFFDDUFFDDUDUDUDUDUDUUUUUUUUU'), 3)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU'), 4)
    test.assert_equals(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU'), 6)