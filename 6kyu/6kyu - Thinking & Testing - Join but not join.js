// 6kyu - Thinking & Testing : Join but not join

/* No Story
No Description
Only by Thinking and Testing
Look at result of testcase, guess the code! */

// Array.prototype.Join = function (arg) {
//     let res = []
//     for (let i = 0; i < this.length; i++) {
//         res.push(this[i])
//         res.push(arg)
//     }
//     return res.slice(0, -1).reduce((a, b) => a.concat(b), [])
// }

Array.prototype.Join = function (separator) {
    return this.reduce((acc, v, i) => i ? acc.concat(separator, v) : [v], [])
}


q = [1, 2, 3].join(1) //      "11213", "")
q
q = [1, 2, 3].Join(1) //      [1, 1, 2, 1, 3], "")
q
q = [1, 2, 3].join([1]) //    "11213", "")
q
q = [1, 2, 3].Join([1]) //    [1, 1, 2, 1, 3], "")
q
q = [1, 2, 3].join("1") //    "11213", "")
q
q = [1, 2, 3].Join("1") //    [1, "1", 2, "1", 3], "")
q
q = [1, 2, 3].join(true) //    "1true2true3", "")
q
q = [1, 2, 3].Join(true) // [1, true, 2, true, 3], "")
q
q = [1, 2, 3].join({}) //    "1[object Object]2[object Object]3", "")
q
q = [1, 2, 3].Join({}) // [1, {}, 2, {}, 3], "")
q
q = [1, 2, 3].join([1, 2]) // "11,221,23", ""
q
q = [1, 2, 3].Join([1, 2]) // [1, 1, 2, 2, 1, 2, 3], "")
q