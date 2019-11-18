// Beta - In order or not?

function order(input) {
    let arr = [...input].map(v => v.charCodeAt() - 94)
    let increasing = arr.every((v, i) => v >= arr[i - 1] || !i)
    let decreasing = arr.every((v, i) => v <= arr[i - 1] || !i)

    return increasing ? 'IN ORDER' :
           decreasing ? 'IN REVERSE ORDER' :
           'OUT OF ORDER'
}

// function order(input) {
//     if ([...input].sort().join('') == input) return 'IN ORDER'
//     if ([...input].sort().reverse().join('') == input) return 'IN REVERSE ORDER'
//     return 'OUT OF ORDER'
// }


q = order('almost') // 'IN ORDER'
q
q = order('cat') // 'OUT OF ORDER'
q
q = order('sponge') // 'IN REVERSE ORDER'
q