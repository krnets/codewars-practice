import codewars_test as test
from kata import find_the_key

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        messages = [ "dance on the table", "hide my beers", "scouts rocks" ];
        secrets =  [ "egncd pn thd tgbud" ,"hked mr bddys" ,"scplts ypcis" ];
        test.assert_equals(find_the_key(messages, secrets) , "agdeikluopry" );