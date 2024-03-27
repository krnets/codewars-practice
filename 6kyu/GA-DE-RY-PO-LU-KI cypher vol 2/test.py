import codewars_test as test
from kata import encode, decode

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(encode("Gug hgs g cgt","gaderypoluki"), "Ala has a cat")
        test.assert_equals(decode("agedyropulik","gaderypoluki"), "gaderypoluki")
        test.assert_equals(encode("Dkucr pu yhr ykbir","politykarenu"), "Dance on the table")
        test.assert_equals(decode("Hmdr nge brres","regulaminowy"), "Hide our beers")
        test.assert_equals(encode("ABCD","gaderypoluki"), "GBCE")
        test.assert_equals(encode("Ala has a cat","gaderypoluki"), "Gug hgs g cgt")