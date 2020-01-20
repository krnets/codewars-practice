// 7kyu - Calculator - Coin Combination

/* The function takes cents value (int) and needs to return the minimum number of coins combination of the same value.

The function should return an array where
coins[0] = pennies ==> $00.01
coins[1] = nickles ==> $00.05
coins[2] = dimes ==> $00.10
coins[3] = quarters ==> $00.25 */

// function coinCombo(cents) {
//     let [pennies, nickles, dimes, quarters] = [[0], [0], [0], [0]]

//     if (cents >= 25) {
//         quarters.push(Math.floor(cents / 25))
//         cents = cents % 25
//     }
//     if (cents >= 10) {
//         dimes.push(Math.floor(cents / 10))
//         cents = cents % 10
//     }
//     if (cents >= 5) {
//         nickles.push(Math.floor(cents / 5))
//         cents = cents % 5
//     }
//     if (cents >= 1) pennies.push(cents / 1)

//     return [pennies, nickles, dimes, quarters].map(v => v.reduce((acc, cur) => acc + cur, 0))
// }

function coinCombo(cents) {
    let [pennies, nickles, dimes, quarters] = [0, 0, 0, 0]

    if (cents >= 25) {
        quarters = Math.floor(cents / 25)
        cents = cents % 25
    }
    if (cents >= 10) {
        dimes = Math.floor(cents / 10)
        cents = cents % 10
    }
    if (cents >= 5) {
        nickles = Math.floor(cents / 5)
        cents = cents % 5
    }
    if (cents >= 1) pennies = cents / 1

    return [pennies, nickles, dimes, quarters]
}

q = coinCombo(1) // [1, 0, 0, 0]
q
q = coinCombo(6) // [1, 1, 0, 0]
q
q = coinCombo(11) // [1, 0, 1, 0]
q
q = coinCombo(101) // [1, 0, 0, 4]
q