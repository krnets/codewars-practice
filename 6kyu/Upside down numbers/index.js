// 6kyu - Upside down numbers

/* Consider the numbers 6969 and 9116. When you rotate them 180 degrees (upside down), these numbers remain the same. 
To clarify, if we write them down on a paper and turn the paper upside down, the numbers will be the same. 
Try it and see! Some numbers such as 2 or 5 don't yield numbers when rotated.

Given a range, return the count of upside down numbers within that range. 
For example, solve(0,10) = 3, because there are only 3 upside down numbers >= 0 and < 10. They are 0, 1, 8.

More examples in the test cases. */

// function solve(x, y) {
//     for (var res = []; x < y; x++)
//         if (![...'23457'].some(n => String(x).includes(n)))
//             res.push(String(x))
//     return res.reduce((s, v) => s + ([...v.replace(/6|9/g, n => n == 6 ? 9 : 6)].reverse().join `` == v), 0)
// }

function solve(x, y) {
    for (var res = []; x < y; x++)
        if (!/[23457]/.test(x))
            res.push(String(x))
    return res.reduce((s, v) => s + ([...v.replace(/6|9/g, n => n == 6 ? 9 : 6)].reverse().join `` == v), 0)
}

// const flip = s => [...s].map(v => "01____9_86" [v]).reverse().join('')
// const solve = (x, y) => Array(y - x).fill().map((_, i) => String(x + i)).filter(v => flip(v) == v).length

// solve=(x,y)=>Array(y - x).fill().map((_,i)=>(x + i)+'').filter(v=>[...v].map(d=>'01----9-86'[d]).reverse().join``==v).length

q = solve(0, 10) // 3
q
q = solve(10, 100) // 4
q
q = solve(100, 1000) // 12
q
q = solve(1000, 10000) // 20
q
q = solve(10000, 15000) // 6
q
q = solve(15000, 20000) // 9
q
q = solve(60000, 70000) // 15
q
q = solve(60000, 130000) // 55
q