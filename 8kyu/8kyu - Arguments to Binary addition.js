// 8kyu - Arguments to Binary addition

/* Given an array add all the number elements and return the binary equivalent of that sum; 
to make the code bullet proof anything else than a number should be addeded as 0 since it can't be addeded.
If your language can handle float binaries assume the array won't contain float or doubles.

arr2bin([1,2]) == '11'
arr2bin([1,2,'a']) == '11'
arr2bin([]) == '0'

NOTE: NaN is a number too in javascript for decimal, binary and n-ary base */

const arr2bin = arr => arr.filter(v => typeof v == 'number').reduce((a, b) => a + b, 0).toString(2)

q = arr2bin([1, 2]) // "11"
q
q = arr2bin([1, 2, 3, 4, 5]) // "1111"
q
q = arr2bin([1, 10, 100, 1000]) // "10001010111"
q
q = arr2bin([null]) // "0"
q
q = arr2bin([true, true, false, 15]) // "1111"
q