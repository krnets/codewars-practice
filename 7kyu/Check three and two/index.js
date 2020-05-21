// 7kyu - Check three and two

/* Given an array with exactly 5 strings "a", "b" or "c" (chars in Java, characters in Fortran), 
check if the array contains three and two of the same values.

["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
["a", "a", "a", "a", "a"] ==> false // 5x "a" */

function checkThreeAndTwo(array) {
    let chars = {}
    array.forEach(c => chars[c] = ++chars[c] || 1)
    let res = Object.values(chars)
    return res.includes(3) && res.includes(2)
}

q = checkThreeAndTwo(["a", "a", "a", "b", "b"]) // true
q
q = checkThreeAndTwo(["a", "c", "a", "c", "b"]) // false
q
q = checkThreeAndTwo(["a", "a", "a", "a", "a"]) // false
q