// 6kyu - Vasya - Clerk

function tickets(peopleInLine) {
    let [count25s, count50s, count100s] = [0,0,0]
    for (let v of peopleInLine) {
        if (v == 25) count25s++
        if (v == 50) {
            count50s++
            count25s--
        }
        if (v == 100) {
            count25s--
            count50s > 0 ? count50s-- : count25s -=2
        }
        if (count25s < 0 || count50s < 0) return 'NO'
    }
    return 'YES'
}

q = tickets([25, 25, 50, 50]) // "YES"
q
q = tickets([25, 100]) // "NO"
q
q = tickets([25,25,25,100,25,50,25,100,25,25,25,100,25,25,25,100])
// 'YES'
q
q = tickets([25,25,25,100,25,25,25,100,25,50,25,100])
// 'YES'
q
q = tickets([25,50,25,100,25,50,25,100,25,50,25,100,25,25,50,100])
//  'YES'
q