import codewars_test as test
from kata import absent_vowel

test.assert_equals(absent_vowel("John Doe hs seven red pples under his bsket"), 0)
test.assert_equals(
    absent_vowel("Bb Smith sent us six neatly arranged range bicycles"), 3
)
