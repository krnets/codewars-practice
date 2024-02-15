import codewars_test as test
from kata import ascii_cipher

test.describe("Basic tests")
test.it("Works with a 'Hello, world'.")
test.assert_equals(ascii_cipher("Hello, world", 18), 
                   "Khoor/#zruog",
                   "Should return 'Khoor/#zruog'")
test.it("Works with a larger key.")
test.assert_equals(ascii_cipher("Encryption rules!", 326), 
                   "hCD",
                   "Should return 'hCD'")
test.it("Works with a negative number.")
test.assert_equals(ascii_cipher("Imitation Game, up in here!", -7), 
                   "BfbmZmbhg@Zf^%nibga^k^",
                   "Should return 'BfbmZmbhg@Zf^%nibga^k^'")