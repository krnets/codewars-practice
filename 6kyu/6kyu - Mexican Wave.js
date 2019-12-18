// 6kyu - Mexican Wave

/* Create a function that turns a string into a Mexican Wave. You will be passed a string and you must 
return that string in an array where an uppercase letter is a person standing up.
Rules
1.  The input string will always be lower case but maybe empty.
2.  If the character in the string is whitespace then pass over it as if it was an empty seat. */

const wave = (str) => [...str].map((_, i) => str.slice(0, i) + str[i].toUpperCase() + str.slice(i + 1)).filter(v => v != str)
// const wave = (str) => Array.from(str, (_, i) => /\s/.test(str[i]) ? null : str.slice(0, i) + str[i].toUpperCase() + str.slice(i + 1)).filter(Boolean);



q = wave("hello")
// ["Hello", "hEllo", "heLlo", "helLo", "hellO"];
q
q = wave("codewars")
// ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"];
q
q = wave("")
// [];
q
q = wave("two words")
// ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"];
q
q = wave(" gap ")
// [" Gap ", " gAp ", " gaP "];
q