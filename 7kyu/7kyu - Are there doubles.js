// 7kyu - Are there doubles?

/* Your job is to build a function which determines whether or not there are double characters in a string 
(including whitespace characters). For example aa, !! or .

You want the function to return true if the string contains double characters and false if not. 
The test should not be case sensitive; for example both aa & aA return true. */

const doubleCheck = (str) => /(.)\1/i.test(str)

q = doubleCheck("abca") // false
q
q = doubleCheck("aabc") // true
q
q = doubleCheck("a 11 c d") // true
q
q = doubleCheck("AabBcC") // true
q
q = doubleCheck("a b  c") // true
q
q = doubleCheck("a b c d e f g h i h k") // false
q
q = doubleCheck("2020") // false
q
q = doubleCheck("a!@€£#$%^&*()_-+=}]{[|\"':;?/>.<,~") // false
q