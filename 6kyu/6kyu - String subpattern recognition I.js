// 6kyu - String subpattern recognition I

/* In this kata you need to build a function to return either true/True 
or false/False if a string can be seen as the repetition of a simpler/shorter subpattern or not.

For example:

hasSubpattern("a") === false; //no repeated pattern
hasSubpattern("aaaa") === true; //created repeating "a"
hasSubpattern("abcd") === false; //no repeated pattern
hasSubpattern("abababab") === true; //created repeating "ab"
hasSubpattern("ababababa") === false; //cannot be entirely reproduced repeating a pattern

Strings will never be empty and can be composed of any character 
(just consider upper and lowercase letters as different entities) and can be pretty long 
(keep an eye on performances!). */


// const hasSubpattern = string => string.match(/^(.*)\1+$/) != null

const hasSubpattern = string => /^(.*)\1+$/.test(string)

// const hasSubpattern = string => string.repeat(2).indexOf(string, 1) != string.length

q = hasSubpattern("a") // false
q
q = hasSubpattern("aaaa") // true
q
q = hasSubpattern("abcd") // false
q
q = hasSubpattern("abababab") // true
q
q = hasSubpattern("ababababa") // false
q
q = hasSubpattern("123a123a123a") // true
q
q = hasSubpattern("123A123a123a") // false
q
q = hasSubpattern("abbaabbaabba") // true
q
q = hasSubpattern("abbabbabba") // false
q
q = hasSubpattern("abcdabcabcd") // false
q