// 7kyu - Training JS #36: methods of Math---kata author's lover:random()

/* Coding in function rndCode. Your task is to generate a random verification code. In accordance with the following rules:

1) the code length should be 8
2) The 1st and 2nd characters should be two uppercase letters. The range is "ABCDEFGHIJKLM"
3) The 3rd-6th characters should be four numbers
4) the 7th and 8th characters should be two symbols. The range is "~!@#$%^&*".
5) If Your code runs 100 times, It should generate 100 non duplicate verification codes

Some valid verification code examples:
AB1234#$ MG6145$@ KJ2249@&
CD5678%^ IG7593~% FH8638@&
EF9012!@ GB7047%$ KD7604^%           */


// function rndCode() {
//     let a = ~~(13 * Math.random() + 65)
//     let b = ~~(13 * Math.random() + 65)
//     let c = ~~(4 * Math.random() + 1)
//     let d = ~~(4 * Math.random() + 1)
//     let e = ~~(4 * Math.random() + 1)
//     let f = ~~(4 * Math.random() + 1)
//     let g = '~!@#$%^&*'
//     let h = ~~(9 * Math.random())
//     let i = ~~(9 * Math.random())
//     return String.fromCharCode(a) + String.fromCharCode(b) + c + d + e + f + g[h] + g[i]
// }

// function choose(str, n) {
//     let output = "";
//     for (let i = 0; i < n; i++) output += str[Math.floor(Math.random() * str.length)];
//     return output;
// }

// function rndCode() {
//     return choose("ABCDEFGHIJKLM", 2) + choose("0123456789", 4) + choose("~!@#$%^&*", 2);
// }

// const choose = (str, n) => Array(n).fill().map((v,i) => str[i] )
// const choose = (str, n) => Array(n).fill().map((_,i) => str[~~(Math.random() * str.length)] )
// const choose = (str, n) => Array.from({ length: n }, ((_, i) => str[~~(Math.random() * str.length)])).join ``
// const choose = (str, n) => Array.from({length: n}, () => str[~~(Math.random() * str.length)]).join ``

// const choose = (str, n) => Array(n).fill().map(() => str[~~(Math.random() * str.length)]).join ``

// const rndCode = () => choose("ABCDEFGHIJKLM", 2) + choose("0123456789", 4) + choose("~!@#$%^&*", 2)

function rndCode() {
    let c = 'ABCDEFGHIJKLM', d = '0123456789', s = '~!@#$%^&*'
    return [c, c, d, d, d, d, s, s].map(v => v[~~(Math.random() * v.length)]).join ``
}

testcode = rndCode()
testcode

q = typeof testcode == "string" // "The result should be string"
q
q = testcode.length == 8 // "The length should be 8"
q
q = "ABCDEFGHIJKLM".indexOf(testcode[0]) > -1 == true // "1st char should generate from A-M"
q
q = "ABCDEFGHIJKLM".indexOf(testcode[1]) > -1 == true // "2nd char should generate from A-M"
q
q = /^\d{4}$/.test(testcode.slice(2, -2)) == true // "3th-6th char should be numbers"
q
q = "~!@#$%^&*".indexOf(testcode[6]) > -1 == true // "7th char should generate from ~!@#$%^&*"
q
q = "~!@#$%^&*".indexOf(testcode[7]) > -1 == true // "8th char should generate from ~!@#$%^&*"
q