// 7kyu - Simple Fun #182: Happy "g"

/* Let's say that "g" is happy in the given string, if there is another "g" immediately to the right or to the left of it.
Find out if all "g"s in the given string are happy.

For str = "gg0gg3gg0gg", the output should be true.
For str = "gog", the output should be false.

    [input] string str
    A random string of lower case letters, numbers and spaces.

    [output] a boolean value
    true if all "g"s are happy, false otherwise. */

// const gHappy = (str) => !/(^|[^g])g(?!g)/.test(str)
// const gHappy = (str) => str.replace(/g{2,}/g, '').match(/g/) == null
const gHappy = str => str.replace(/g{2,}/g, '').search('g') < 0


q = gHappy("gg0gg3gg0gg") // true
q
q = gHappy("gog") // false
q
q = gHappy("ggg ggg g ggg") // false
q
q = gHappy("A half of a half is a quarter.") // true
q
q = gHappy("good grief") // false
q
q = gHappy("bigger is ggooder") // true
q
q = gHappy("gggggggggg") // true
q