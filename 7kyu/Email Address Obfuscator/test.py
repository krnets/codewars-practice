import codewars_test as test
from kata import obfuscate

test.describe("Example Tests")
test.assert_equals(obfuscate('test@123.com'), 'test [at] 123 [dot] com')
test.assert_equals(obfuscate('Code_warrior@foo.ac.uk'), 'Code_warrior [at] foo [dot] ac [dot] uk')
