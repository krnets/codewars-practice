// 7kyu - Substring fun

/* Function nthChar takes 1 parameter - an array of words.
You must concatenate the nth letter from each word to 
construct a new word which should be returned as a string.
Test cases contain valid input only - i.e. a string array or an empty array, 
each word will have at least as many letters as its ordinal position. */

const nthChar = words => words.map((v, i) => v[i]).join ``

q = nthChar(['yes', 'yes', 'yes']) // 'yes'
q