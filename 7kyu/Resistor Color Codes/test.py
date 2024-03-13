import codewars_test as test
from kata import decode_resistor_colors

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("A resistor under 1000 ohms and with only three bands")   
    def basic_test_cases():
        test.assert_equals(decode_resistor_colors("yellow violet black"), "47 ohms, 20%")
    @test.it("A resistor between 1000 and 999999 ohms, with a gold fourth band")   
    def basic_test_cases():
        test.assert_equals(decode_resistor_colors("yellow violet red gold"), "4.7k ohms, 5%")
    @test.it("A resistor of 1000000 ohms or above, with a silver fourth band") 
    def basic_test_cases():  
        test.assert_equals(decode_resistor_colors("brown black green silver"), "1M ohms, 10%")
    @test.it("Some additional common resistor values")
    def basic_test_cases():
        test.assert_equals(decode_resistor_colors("brown black black"), "10 ohms, 20%")
        test.assert_equals(decode_resistor_colors("brown black brown gold"), "100 ohms, 5%")
        test.assert_equals(decode_resistor_colors("red red brown"), "220 ohms, 20%")
        test.assert_equals(decode_resistor_colors("orange orange brown gold"), "330 ohms, 5%")
        test.assert_equals(decode_resistor_colors("yellow violet brown silver"), "470 ohms, 10%")
        test.assert_equals(decode_resistor_colors("blue gray brown"), "680 ohms, 20%")
        test.assert_equals(decode_resistor_colors("brown black red silver"), "1k ohms, 10%")
        test.assert_equals(decode_resistor_colors("brown black orange"), "10k ohms, 20%")
        test.assert_equals(decode_resistor_colors("red red orange silver"), "22k ohms, 10%")
        test.assert_equals(decode_resistor_colors("yellow violet orange gold"), "47k ohms, 5%")
        test.assert_equals(decode_resistor_colors("brown black yellow gold"), "100k ohms, 5%")
        test.assert_equals(decode_resistor_colors("orange orange yellow gold"), "330k ohms, 5%")
        test.assert_equals(decode_resistor_colors("red black green gold"), "2M ohms, 5%")