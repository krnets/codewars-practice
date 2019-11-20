// 6kyu - Repeated Substring

/* For a given nonempty string s find a minimum substring t and the maximum number k, 
such that the entire string s is equal to t repeated k times. 
The input string consists of lowercase latin letters. 
Your function should return an array [t, k] */


// function f(s) {
//     let arr = [...s]
//     if (s == 'abceeeabc') return [s, 1]
//     for (let i = 0; i < arr.length; i++)
//         if (arr.every((v, idx) => v == arr[idx % i]))
//             return [t = arr.slice(0, i).join ``, ~~(s.length / t.length)]
//     return [s, 1]
// }

// function f(s) {
//     for (let i = s.length - 1; i >= 0; i--)
//         if (s.split(s.slice(i)).filter(v => v.length > 0).length == 0)
//             return [s.slice(i), (s.length / s.slice(i).length)]
// }

// function f(s) {
//     for (let i = s.length - 1; i >= 0; i--)
//         if (s.split(s.substr(i)).filter(e => e.length > 0).length == 0)
//             return [s.substr(i), s.length / s.substr(i).length]
// }

// const f = s => /^(.+)\1+$/.test(s) ? [s.replace(/^(.+?)\1+/, '$1'), s.match(/(.+?)(?=\1)/g).length + 1] : [s, 1]
// const f = (s, r) => [r = s.match(/^(.+?)\1*$/)[1], s.length / r.length]
// const f = s => [r = s.match(/(..*?)(?=\1*$)/g)[0], s.length / r.length]
// const f = s => [r = s.match(/^(.+?)\1*$/)[1], s.length / r.length]
const f = s => (r = s.match(/(..*?)(?=\1*$)/g), [r[0], r.length])


q = f("ababab") // ["ab", 3]
q
q = f("abcde") // ["abcde", 1]
q