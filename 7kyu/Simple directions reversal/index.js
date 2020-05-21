// 7kyu - Simple directions reversal

// In this Kata, you will be given directions and your task will be to find your way back

function solve(arr) {
    let wayback = []
    let sections = arr.map(v => v.split(' on '))
    let dict = { Begin: 'Begin', Left: 'Right', Right: 'Left' }
    for (let i = 0; i < arr.length; i++)
        wayback.unshift(dict[sections[(i + 1) % arr.length][0]] + ' on ' + sections[i][1])
    return wayback
}

q = solve(['Begin on 3rd Blvd', 'Right on First Road', 'Left on 9th Dr'])
//  ['Begin on 9th Dr', 'Right on First Road', 'Left on 3rd Blvd'])
q
q = solve(["Begin on Road A", "Right on Road B", "Right on Road C", "Left on Road D"])
// ['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A'])
q
q = solve(['Begin on Road A']) // ['Begin on Road A']
q