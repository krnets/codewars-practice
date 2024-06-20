import codewars_test as test
from kata import mutate_my_strings

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(mutate_my_strings("", "") , "\n")
        test.assert_equals(mutate_my_strings("bubble gum", "bubble gum") , "bubble gum\n")
        test.assert_equals(mutate_my_strings("bubble gum", "turtle ham") , "bubble gum\ntubble gum\nturble gum\nturtle gum\nturtle hum\nturtle ham\n")
        test.assert_equals(mutate_my_strings("car door", "car bore") , "car door\ncar boor\ncar borr\ncar bore\n")
        test.assert_equals(mutate_my_strings("open source", "lean course") , "open source\nlpen source\nleen source\nlean source\nlean cource\nlean course\n")
        test.assert_equals(mutate_my_strings("right wrong", "wrong right") , "right wrong\nwight wrong\nwrght wrong\nwroht wrong\nwront wrong\nwrong wrong\nwrong rrong\nwrong riong\nwrong rigng\nwrong righg\nwrong right\n")
        test.assert_equals(mutate_my_strings("pythons best", "jscript bttr") , "pythons best\njythons best\njsthons best\njschons best\njscrons best\njscrins best\njscrips best\njscript best\njscript btst\njscript bttt\njscript bttr\n")
        test.assert_equals(mutate_my_strings("acvqwrtqwcasd", "lvqewnhuiypaf") , "acvqwrtqwcasd\nlcvqwrtqwcasd\nlvvqwrtqwcasd\nlvqqwrtqwcasd\nlvqewrtqwcasd\nlvqewntqwcasd\nlvqewnhqwcasd\nlvqewnhuwcasd\nlvqewnhuicasd\nlvqewnhuiyasd\nlvqewnhuiypsd\nlvqewnhuiypad\nlvqewnhuiypaf\n")
        test.assert_equals(mutate_my_strings("bubble gum crisis", "turtle ham creamy") ,"bubble gum crisis\ntubble gum crisis\nturble gum crisis\nturtle gum crisis\nturtle hum crisis\nturtle ham crisis\nturtle ham cresis\nturtle ham creais\nturtle ham creams\nturtle ham creamy\n")
        test.assert_equals(mutate_my_strings("bubble gum crisis tokyo 2040", "turtle ham creamy apple pies") , "bubble gum crisis tokyo 2040\ntubble gum crisis tokyo 2040\nturble gum crisis tokyo 2040\nturtle gum crisis tokyo 2040\nturtle hum crisis tokyo 2040\nturtle ham crisis tokyo 2040\nturtle ham cresis tokyo 2040\nturtle ham creais tokyo 2040\nturtle ham creams tokyo 2040\nturtle ham creamy tokyo 2040\nturtle ham creamy aokyo 2040\nturtle ham creamy apkyo 2040\nturtle ham creamy appyo 2040\nturtle ham creamy applo 2040\nturtle ham creamy apple 2040\nturtle ham creamy apple p040\nturtle ham creamy apple pi40\nturtle ham creamy apple pie0\nturtle ham creamy apple pies\n")