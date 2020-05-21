// 7kyu - Partial Word Searching

/* Write a method that will search an array of strings for all strings that contain another string, 
ignoring capitalization. Then return an array of the found strings.

The method takes two parameters, the query string and the array of strings to search, and returns an array.

If the string isn't contained in any of the strings in the array, the method returns an array containing 
a single string: "Empty" (or Nothing in Haskell, or "None" in Python and C)

If the string to search for is "me", and the array to search is ["home", "milk", "Mercury", "fish"], 
the method should return ["home", "Mercury"]. */

// function wordSearch(query, seq) {
//   let re = new RegExp(query, "i");
//   let filtered = seq.filter(v => re.test(v));
//   return filtered.length == 0 ? ["Empty"] : filtered;
// }

// const wordSearch = (query, seq) => (arr = seq.filter(v => new RegExp(query, "i").test(v))).length ? arr : ["Empty"];

const wordSearch = (query, seq) => (arr = seq.filter(v => v.match(new RegExp(query, "i")))).length ? arr : ["Empty"];

q = wordSearch("ab", ["za", "ab", "abc", "zab", "zbc"]) // ["ab", "abc", "zab"]
q
q = wordSearch("aB", ["za", "ab", "abc", "zab", "zbc"]) // ["ab", "abc", "zab"]
q
q = wordSearch("ab", ["za", "aB", "Abc", "zAB", "zbc"]) // ["aB", "Abc", "zAB"]
q
q = wordSearch("abcd", ["za", "aB", "Abc", "zAB", "zbc"]) // ["Empty"]
q