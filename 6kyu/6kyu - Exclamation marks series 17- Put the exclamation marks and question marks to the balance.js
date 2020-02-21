// 6kyu - Exclamation marks series #17: Put the exclamation marks and question marks to the balance, Are they balanced?

/* Each exclamation mark weight is 2; Each question mark weight is 3. 
Put two string left and right to the balance, Are they balanced?

If the left side is more heavy, return "Left"; If the right side is more heavy, return "Right"; 
If they are balanced, return "Balance".

balance("!!","??") === "Right"
balance("!??","?!!") === "Left"
balance("!?!!","?!?") === "Left"
balance("!!???!????","??!!?!!!!!!!") === "Balance"

Please don't post issue about difficulty or duplicate.  */

// function balance(left, right) {
//     let leftSum = [...left].reduce((a, b) => a + (b == '!' ? 2 : 3), 0)
//     let rightSum = [...right].reduce((a, b) => a + (b == '?' ? 3 : 2), 0)
//     return leftSum < rightSum ? 'Right' : leftSum > rightSum ? 'Left' : 'Balance'
// }

function balance(left, right) {
    const weight = s => [...s].reduce((acc, v) => acc + (v == '!' ? 2 : v == '?' ? 3 : 0), 0)
    let diff = weight(left) - weight(right)
    return diff == 0 ? 'Balance' : diff > 0 ? 'Left' : 'Right'
}

q = balance("!!", "??") // "Right"
q
q = balance("!??", "?!!") // "Left"
q
q = balance("!?!!", "?!?") // "Left"
q
q = balance("!!???!????", "??!!?!!!!!!!") // "Balance"
q