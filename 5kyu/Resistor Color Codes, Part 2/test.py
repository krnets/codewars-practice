import codewars_test as test
from kata import encode_resistor_colors

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Some common resistor values")
    def basic_test_cases():
        test.assert_equals(encode_resistor_colors("10 ohms"), "brown black black gold")
        test.assert_equals(encode_resistor_colors("47 ohms"), "yellow violet black gold")
        test.assert_equals(encode_resistor_colors("100 ohms"), "brown black brown gold")
        test.assert_equals(encode_resistor_colors("220 ohms"), "red red brown gold")
        test.assert_equals(encode_resistor_colors("330 ohms"), "orange orange brown gold")
        test.assert_equals(encode_resistor_colors("470 ohms"), "yellow violet brown gold")
        test.assert_equals(encode_resistor_colors("680 ohms"), "blue gray brown gold")
        test.assert_equals(encode_resistor_colors("1k ohms"), "brown black red gold")
        test.assert_equals(encode_resistor_colors("4.7k ohms"), "yellow violet red gold")
        test.assert_equals(encode_resistor_colors("10k ohms"), "brown black orange gold")
        test.assert_equals(encode_resistor_colors("22k ohms"), "red red orange gold")
        test.assert_equals(encode_resistor_colors("47k ohms"), "yellow violet orange gold")
        test.assert_equals(encode_resistor_colors("100k ohms"), "brown black yellow gold")
        test.assert_equals(encode_resistor_colors("330k ohms"), "orange orange yellow gold")
        test.assert_equals(encode_resistor_colors("1M ohms"), "brown black green gold")
        test.assert_equals(encode_resistor_colors("2M ohms"), "red black green gold")
        test.assert_equals(encode_resistor_colors('4.1M ohms'), 'yellow black green gold')
