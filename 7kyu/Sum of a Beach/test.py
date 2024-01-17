import codewars_test as test
from kata import sum_of_a_beach

test.assert_equals(sum_of_a_beach("SanD"), 1)
test.assert_equals(sum_of_a_beach("sunshine"), 1)
test.assert_equals(sum_of_a_beach("sunsunsunsun"), 4)
test.assert_equals(sum_of_a_beach("123FISH321"), 1)

test.assert_equals(sum_of_a_beach("WAtErSlIde"), 1)
test.assert_equals(sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN"), 3)
test.assert_equals(sum_of_a_beach("gOfIshsunesunFiSh"), 4)
test.assert_equals(sum_of_a_beach("cItYTowNcARShoW"), 0)
