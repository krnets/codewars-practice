// 6kyu - Word a10n (abbreviation)

/* The word i18n is a common abbreviation of internationalization in the developer community, 
used instead of typing the whole word and trying to spell it correctly. 
Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all "words" (see below) within that string of 
length 4 or greater into an abbreviation, following these rules:

    A "word" is a sequence of alphabetical characters. By this definition, any other character like a 
    space or hyphen (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
    The abbreviated version of the word should have the first letter, then the number of removed characters, 
    then the last letter (eg. "elephant ride" => "e6t r2e").

abbreviate("elephant-rides are really fun!")
//          ^^^^^^^^*^^^^^*^^^*^^^^^^*^^^*
// words (^):   "elephant" "rides" "are" "really" "fun"
//                123456     123     1     1234     1
// ignore short words:               X              X

// abbreviate:    "e6t"     "r3s"  "are"  "r4y"   "fun"
// all non-word characters (*) remain in place
//                     "-"      " "    " "     " "     "!"
=== "e6t-r3s are r4y fun!"
Fundamentals | Strings */

// const abbreviate = (string) => string.replace(/[a-z]{4,}/gi, v => (v[0] + (v.length - 2) + v.slice(-1)))
const abbreviate = (string) => string.replace(/\B\w{2,}\B/g, match => match.length)
// const abbreviate = (string) => string.match(/\B\w{2,}\B/g) // neat solution with not-word boundary


q = abbreviate("internationalization") // "i18n"
q
q = abbreviate("accessibility") // "a11y"
q
q = abbreviate("Accessibility") // "A11y"
q
q = abbreviate("elephant-ride") // "e6t-r2e"
q
q = abbreviate("You need, need not want, to complete this code-wars mission")
//  'You n2d, n2d not w2t, to c6e t2s c2e-w2s m5n'
q
q = abbreviate("monolithic doggy a")
// 'm8c d3y a'
q
q = abbreviate("is a")
// 'is a'
q
q = abbreviate("a")
// 'a'
q
q = abbreviate("doggy sat sat mat")
// 'd3y sat sat mat'
q
q = abbreviate("mat monolithic a cat")
// 'mat m8c a cat', instead got: 'm18t'
q
q = abbreviate("on cat on is double-barreled sits")
// 'on cat on is d4e-b6d s2s'
q
q = abbreviate("cat double-barreled the doggy the double-barreled monolithic mat")
// 'cat d4e-b6d the d3y the d4e-b6d m8c mat'
q
q = abbreviate("cat")
// 'cat'
q
q = abbreviate("is on sits sits cat the sits a")
// 'is on s2s s2s cat the s2s a'
q
q = abbreviate("monolithic cat sat sits")
// 'm8c cat sat s2s'
q
q = abbreviate("double-barreled a sits")
// 'd4e-b6d a s2s'
q