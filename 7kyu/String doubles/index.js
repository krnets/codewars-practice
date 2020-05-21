// 7kyu - String doubles

/* In this Kata, you will write a function doubles that will remove double string characters that are adjacent to each other.

doubles('abbcccdddda') = 'aca', because, from left to right:

a) There is only one 'a' on the left hand side, so it stays.
b) The 2 b's disapper because we are removing double characters that are adjacent. 
c) Of the 3 c's, we remove two. We are only removing doubles. 
d) The 4 d's all disapper, because we first remove the first double, and again we remove the second double.
e) There is only one 'a' at the end, so it stays.

Two more examples: doubles('abbbzz') = 'ab' and doubles('abba') = "". 
In the second example, when we remove the b's in 'abba', the double a that results is then removed.

The strings will contain lowercase letters only. More examples in the test cases.  */

// function doubles(str) {
//     let res = []
//     for (let ch of str) {
//         if (res.length != 0 && res[res.length - 1] == ch)
//             res.pop()
//         else
//             res.push(ch)
//     }
//     return res.join('')
// }

// function doubles(s) {
//     while (/(.)\1/.test(s))
//         s = s.replace(/(.)\1/, '')
//     return s
// }

// const doubles = str => (x = str.replace(/(\w)\1/g, '')) == str ? str : doubles(x)


q = doubles('abbbzz') // 'ab'
q
q = doubles('zzzzykkkd') // 'ykd'
q
q = doubles('abbcccdddda') // 'aca'
q
q = doubles('vvvvvoiiiiin') // 'voin'
q
q = doubles('rrrmooomqqqqj') // 'rmomj'
q
q = doubles('xxbnnnnnyaaaaam') // 'bnyam'
q