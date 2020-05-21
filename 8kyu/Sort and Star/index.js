// 8kyu - Sort and Star

/* You will be given an vector of string(s). You must sort it alphabetically (case-sensitive!!) and then return the first value.
The returned value must be a string, and have "***" between each of its letters.
You should not remove or add elements from/to the array. */

function twoSort(s) {
    return s.sort()[0].split('').join('***')
}

q = twoSort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"])
//  'b***i***t***c***o***i***n' 
q
q = twoSort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"])
//  'a***r***e'
q