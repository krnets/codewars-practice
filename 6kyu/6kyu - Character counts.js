// 6kyu - Character counts

/* The object is to count the number of occurances of a specified character (or set of characters) in a string.
Instructions

Complete the placeholder function characterCount.

    it should return the number of times a single character appears in the string, or
    if multiple characters are specified (either by providing an array or string of length 2 or more), it should return an array of character counts
    see the unit tests provided for a more comprehensive definition

NOTE: The tests assume that if no arguments are provided to the function (i.e. ''.characterCount()), then the result is undefined.
Algorithms | Fundamentals | Strings */

String.prototype.characterCount = function (charsToCount) {
    if (!charsToCount) return undefined
    let dict = {};
    [...this].forEach(v => dict[v] = ++dict[v] || 1)
    let res = [...charsToCount].reduce((arr, v) => (arr.push(dict[v] || 0), arr), [])
    return res.length > 1 ? res : res[0]
}

// String.prototype.characterCount = function (charsToCount) {
//     return charsToCount ? [...charsToCount].map(c => this.split(c).length - 1).reduce((arr, v) => [].concat(arr, v)) : void 0
// }

q = typeof ''.characterCount;
q
q = ''.characterCount() // undefined
q
q = 'lol'.characterCount('l') // 2
q
q = 'booop-booop-deee-doo-dooop'.characterCount('ado') // [0,3,11]
q
q = 'booop-booop-deee-doo-dooop'.characterCount(['a', 'd', 'o', 'o', 'd', 'a']) // [0,3,11,11,3,0]);
q