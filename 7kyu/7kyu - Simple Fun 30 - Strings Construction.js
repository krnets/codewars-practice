// 7kyu - Simple Fun #30: Strings Construction

/* How many strings equal to A can be constructed using letters from the string B? 
Each letter can be used only once and in one string only.

For A = "abc" and B = "abccba", the output should be 2.

We can construct 2 strings A with letters from B.

    [input] string A
    String to construct, A contains only lowercase English letters.
    Constraints: 3 ≤ A.length ≤ 9.

    [input] string B
    String containing needed letters, B contains only lowercase English letters.
    Constraints: 3 ≤ B.length ≤ 50.

    [output] an integer */

// let re = new RegExp(`[${A}]`, 'g')
// let matchFoundInB = B.match(re) || []
// if (matchFoundInB.length == 0) return 0;
// matchFoundInB.forEach(v => countLettersB[v] = ++countLettersB[v] || 1)
// if (countLettersA.hasOwnProperty(key))

function stringsConstruction(A, B) {
    let res = [];
    let countCharsA = {};
    let countCharsB = {};
    [...A].forEach(v => countCharsA[v] = ++countCharsA[v] || 1);
    [...B].forEach(v => countCharsB[v] = ++countCharsB[v] || 1);

    for (let key in countCharsA)
        res.push(countCharsB[key] / countCharsA[key])

    return Math.min(...res) | 0
}

// function stringsConstruction(A, B) {
//     for (let i = 0;; i++) {
//         for (let char of A) {
//             if (B.includes(char))
//                 B = B.replace(char, '')
//             else return i
//         }
//     }
// }

q = stringsConstruction("abc", "abccba") // 2
q
q = stringsConstruction("hnccv", "hncvohcjhdfnhonxddcocjncchnvohchnjohcvnhjdhihsn") // 3
q
q = stringsConstruction("abc", "def") // 0
q
q = stringsConstruction("zzz", "zzzzzzzzzzz") // 3
q