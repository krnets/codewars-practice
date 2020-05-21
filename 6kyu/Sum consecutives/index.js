// 6kyu - Sum consecutives

// const sumConsecutives = s => s.reduce((acc, curr, i) => {
//     if (curr != s[i - 1]) acc.push(curr);
//     else acc[acc.length - 1] += curr;
//     return acc
// }, [])

// const sumConsecutives = s => s.reduce((a,v,i) => { (v != s[i-1]) ? a.push(v) : a[a.length-1] += v; return a }, [])

const sumConsecutives = s => s.reduce((a,v,i) => (v != s[i-1] ? a.push(v) : a[a.length-1] += v, a), [])

// const sumConsecutives = s => s.reduce((a,v,i) => (v == s[i-1] ? a[a.length-1] += v : a.push(v), a), [])


// function sumConsecutives(s) {
//     let sum = 0
//     let sums = []
//     for (let i = 0; i < s.length; i++) {
//         sum += s[i]
//         if (s[i] != s[i + 1]) {
//             sums.push(sum)
//             sum = 0
//         }
//     }
//     return sums
// }

q = sumConsecutives([1, 4, 4, 4, 0, 4, 3, 3, 1]) // [1, 12, 0, 4, 6, 1], "on list [1,4,4,0,4,3,3,1] you get "
q
q = sumConsecutives([1, 1, 7, 7, 3]) // [2, 14, 3], "on list [1,1,7,7,3] you get "
q
q = sumConsecutives([-5, -5, 7, 7, 12, 0]) // [-10, 14, 12, 0], "on list [-5,-5,7,7,12,0] you get "
q
q = sumConsecutives([3, 3, 3, 3, 1]) // [12, 1], "on list [3,3,3,3,1] you get "
q