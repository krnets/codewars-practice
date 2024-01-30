from kata import transpose_two_strings
import codewars_test as test

@test.describe("Transpose strings")
def transpose_strings():
    
    @test.it("Basic tests")
    def basic_tests():
        test.assert_equals(transpose_two_strings(["Hello","World"]), "H W\ne o\nl r\nl l\no d")
        test.assert_equals(transpose_two_strings(["joey","louise"]), "j l\no o\ne u\ny i\n  s\n  e")
        test.assert_equals(transpose_two_strings(["a","cat"]), "a c\n  a\n  t")
        test.assert_equals(transpose_two_strings(["cat",""]), "c  \na  \nt  ")
        test.assert_equals(transpose_two_strings(["!a!a!","?b?b"]), "! ?\na b\n! ?\na b\n!  ")