import codewars_test as test
from kata import part

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(part(["Grouse", "Partridge", "Pheasant"]), "Mine's a Pint!")
        test.assert_equals(part(["Pheasant", "Goose", "Starling", "Robin"]), "Lynn, I've pierced my foot on a spike!!")
        test.assert_equals(part(["Grouse", "Partridge", "Partridge", "Partridge", "Pheasant"]), "Mine's a Pint!!!")
        test.assert_equals(part([]), "Lynn, I've pierced my foot on a spike!!")
        test.assert_equals(part(["Grouse", "Partridge", "Pheasant", "Goose", "Starling", "Robin", "Thrush", "Emu", "PearTree", "Chat", "Dan", "Square", "Toblerone", "Lynn", "AlphaPapa", "BMW", "Graham", "Tool", "Nomad", "Finger", "Hamster"]), "Mine's a Pint!!!!!!!!")
