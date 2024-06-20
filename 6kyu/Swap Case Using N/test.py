import codewars_test as test
from kata import swap

@test.it('Basic Test Cases')
def basic_tests():
    test.assert_equals(swap('Hello world!', 11), 'heLLO wORLd!')
    test.assert_equals(swap('the quick broWn fox leapt over the fence',9),'The QUicK BrowN foX LeaPT ovER thE FenCE')
    test.assert_equals(swap('eVerybody likes ice cReam',85),'EVErYbODy LiKeS IcE creAM')
    test.assert_equals(swap('gOOd MOrniNg',7864),'GooD MorNIng')
    test.assert_equals(swap('how are you today?',12345),'HOw are yoU TOdaY?')
    
@test.it('Edge Cases')
def edge_case_tests():
    test.assert_equals(swap('the lord of the rings', 0), 'the lord of the rings')
    test.assert_equals(swap('',11345),'')