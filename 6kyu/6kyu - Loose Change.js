// 6kyu - Loose Change

// function looseChange(cents) {
//     cents = Math.floor(cents)

//     let remaining = 0

//     let coinsValue = {
//         Nickels: 0.05,
//         Pennies: 0.01,
//         Dimes: 0.10,
//         Quarters: 0.25
//     }
//     let coinsTotal = {
//         Nickels: 0,
//         Pennies: 0,
//         Dimes: 0,
//         Quarters: 0
//     }

//     if (cents < 0)
//         return coinsTotal

//     while (cents > 0) {
//         remaining = cents - (coinsValue.Quarters * 100)
//         if (remaining >= 0) {
//             cents = remaining
//             coinsTotal.Quarters++
//         } else {
//             remaining = cents - (coinsValue.Dimes * 100)
//             if (remaining >= 0) {
//                 cents = remaining
//                 coinsTotal.Dimes++
//             } else {
//                 remaining = cents - (coinsValue.Nickels * 100)
//                 if (remaining >= 0) {
//                     cents = remaining
//                     coinsTotal.Nickels++
//                 } else {
//                     cents = cents - (coinsValue.Pennies * 100)
//                     coinsTotal.Pennies++
//                 }
//             }
//         }
//     }
//     return coinsTotal
// }

function looseChange(cents) {
    let coins = {
        Quarters: 25,
        Dimes: 10,
        Nickels: 5,
        Pennies: 1,
    }

    let change = {
        Quarters: 0,
        Dimes: 0,
        Nickels: 0,
        Pennies: 0,
    }

    for (let c in coins) {
        while (cents >= coins[c]) {
            cents -= coins[c]
            change[c]++
        }
    }
    return change
}

// function looseChange(c) {
//     let res = [0, 0, 0, 0]
//     let i = 0
//     let AMTS = [25, 10, 5, 1]
//     let COINS = ['Quarters', 'Dimes', 'Nickels', 'Pennies']

//     while (c >= 1) {
//         while (c >= AMTS[i]) {
//             c -= AMTS[i]
//             res[i]++
//         }
//         i++
//     }
//     return res.reduce((acc, c, i) => ({
//         ...acc,
//         [COINS[i]]: c
//     }), {})
// }

// const looseChange = (cents) => (
//     cents = Math.max(cents, 0), 
//     {
//         Quarters: cents / 25 | 0,
//         Dimes: cents % 25 / 10 | 0,
//         Nickels: cents % 25 % 10 / 5 | 0,
//         Pennies: cents % 5 | 0
//     })

// const looseChange = cents => {
//     let obj = { 'Quarters': 0, 'Dimes': 0, 'Nickels': 0, 'Pennies': 0 }
//     let val = [25, 10, 5, 1]
//     let i = 0
//     if (cents <= 0) return obj
//     for (let coin in obj) {
//         obj[coin] = cents / val[i] | 0
//         cents -= obj[coin] * val[i]
//         i++
//     }
//     return obj
// }

// function looseChange(cents) {
//     cents = Math.floor(Math.max(cents, 0))

//     let quarters = Math.floor(cents / 25)
//     cents -= quarters * 25
//     let dimes = Math.floor(cents / 10)
//     cents -= dimes * 10
//     let nickles = Math.floor(cents / 5)
//     cents -= nickles * 5
//     let pennies = cents

//     return { 'Nickels': nickles, 'Pennies': pennies, 'Dimes': dimes, 'Quarters': quarters }
// }

q = looseChange(56) // {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2})
q
q = looseChange(100) // {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 4})
q
q = looseChange(0) // {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
q
q = looseChange(-3) // {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}),"no looseChange for -3 cents"
q
q = looseChange(7.9) // {'Nickels': 1, 'Pennies': 2, 'Dimes': 0, 'Quarters': 0}),"7.9 cents should be rounded down to 7"
q