from kata import calculator as calc
import codewars_test as test


def tester(input, expected, optional_message=""):
    test.assert_equals(input, expected, optional_message)


@test.describe("Dot Calculator Sample Tests")
def ExampleTests():
    @test.it("Sample Tests")
    def run_sample_tests():
        tester(calc("..... + ..............."), "....................")
        tester(calc("..... - ..."), "..")
        tester(calc("..... - ."), "....")
        tester(calc("..... * ..."), "...............")
        tester(calc("..... * .."), "..........")
        tester(calc("..... // .."), "..")
        tester(calc("..... // ."), ".....")
        tester(calc(". // .."), "")
        tester(calc(". - ."), "")
