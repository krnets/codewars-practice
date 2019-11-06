// 6kyu - Simple number divisibility

// function permute(string) {
//     let array = []
//     for (let i = 0; i < Math.pow(string.length, 4); i++)
//         array.push([...string].sort(() => 0.5 - Math.random()))
//     return [...new Set(array.map((v => v.join ``)))]
// }

function solve(n) {
    let count = 0
    n

    if (n < 25 && n % 25 != 0)
        return -1

    if (n % 25 == 0)
        return 0

    const moveDigitLeft = n => {
        let aa = String(n)
        aa
        let bb = aa.slice(-1)
        bb
        let cc = aa.slice(0,)

    }
    // let a = permute(String(n))
    let a = moveDigitLeft(n)
    a
    
    let b = 0

    for (let i = 0; i < a.length; i++) {
        b
        b = a[i]
        if (b % 25 == 0) {
            b
            count++
        }
    }

    return count
}

// q = solve(521) // 3
// q
// q = solve(100) // 0
// q
// q = solve(1) // -1
// q