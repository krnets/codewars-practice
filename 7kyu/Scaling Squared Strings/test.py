import codewars_test as test
from kata import scale

def testing(actual, expected):
    test.assert_equals(actual, expected)
    
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        a = "abcd\nefgh\nijkl\nmnop"
        r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
        testing(scale(a, 2, 3), r)

        testing(scale("", 5, 5), "")

        testing(scale("Kj\nSH", 1, 2),"Kj\nKj\nSH\nSH")

        testing(scale("lxnT\nqiut\nZZll\nFElq", 1, 2), "lxnT\nlxnT\nqiut\nqiut\nZZll\nZZll\nFElq\nFElq")

        r = ("YYVVjjoossWW\nYYVVjjoossWW\nHHGGhhKKGGZZ\nHHGGhhKKGGZZ\nLLHHNNMMLLmm\nLLHHNNMMLLmm\nJJttccWWCCjj\n"
                "JJttccWWCCjj\nggVVttjjyykk\nggVVttjjyykk\nOOJJBBkkOOKK\nOOJJBBkkOOKK")
        testing(scale("YVjosW\nHGhKGZ\nLHNMLm\nJtcWCj\ngVtjyk\nOJBkOK", 2, 2), r)

        r = "YVjosW\nYVjosW\nHGhKGZ\nHGhKGZ\nLHNMLm\nLHNMLm\nJtcWCj\nJtcWCj\ngVtjyk\ngVtjyk\nOJBkOK\nOJBkOK"
        testing(scale("YVjosW\nHGhKGZ\nLHNMLm\nJtcWCj\ngVtjyk\nOJBkOK", 1, 2), r)

        testing(scale("WgaB\nMmIn\nqJwv\nAhho", 2, 1), "WWggaaBB\nMMmmIInn\nqqJJwwvv\nAAhhhhoo")

        testing(scale("CG\nla", 2, 3), "CCGG\nCCGG\nCCGG\nllaa\nllaa\nllaa")    