import codewars_test as test
from kata import encrypt, decrypt

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('encrypt')
    def basic_test_cases():
        test.assert_equals(encrypt("This is a test!", 0), "This is a test!")
        test.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
        test.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
        test.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
        test.assert_equals(encrypt("This is a test!", 4), "This is a test!")
        test.assert_equals(encrypt("This is a test!", -1), "This is a test!")
        test.assert_equals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")
        
    @test.it('decrypt')
    def basic_test_cases():
        test.assert_equals(decrypt("This is a test!", 0), "This is a test!")
        test.assert_equals(decrypt("hsi  etTi sats!", 1), "This is a test!")
        test.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
        test.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
        test.assert_equals(decrypt("This is a test!", 4), "This is a test!")
        test.assert_equals(decrypt("This is a test!", -1), "This is a test!")
        test.assert_equals(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")
        
    @test.it('Empty strings and invalid cases')
    def basic_test_cases():
        test.assert_equals(encrypt("", 0), "")
        test.assert_equals(decrypt("", 0), "")
        test.assert_equals(encrypt(None, 0), None)
        test.assert_equals(decrypt(None, 0), None)