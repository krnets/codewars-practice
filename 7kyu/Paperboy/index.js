// 7kyu - Paperboy

/* You and your best friend Stripes have just landed your first high school jobs! You'll be delivering newspapers to your 
neighbourhood on weekends. For your services you'll be charging a set price depending on the quantity of the newspaper bundles.

The cost of deliveries is:

    $3.85 for 40 newspapers
    $1.93 for 20
    $0.97 for 10
    $0.49 for 5
    $0.10 for 1

Stripes is taking care of the footwork doing door-to-door drops and your job is to take care of the finances. 
What you'll be doing is providing the cheapest possible quotes for your services.

Write a function that's passed an integer representing the amount of newspapers and returns the cheapest price. 
The returned number must be rounded to two decimal places. */

// function cheapestQuote(newspapers) {
//     let total = 0
//     let cost = [ [40, 3.85], [20, 1.93], [10, 0.97], [5, 0.49], [1, 0.10] ]
//     for (let i = 0; i < cost.length; i++) {
//         if (newspapers >= cost[i][0]) {
//             total += ~~(newspapers / cost[i][0]) * cost[i][1]
//             newspapers %= cost[i][0]
//         }
//     }
//     return +total.toFixed(2)
// }

function cheapestQuote(newspapers) {
    let sum = 0
    let cost = { 40: 3.85, 20: 1.93, 10: 0.97, 5: 0.49, 1: 0.10 }

    Object.keys(cost).reverse().forEach(amount => {
        if (newspapers / amount > 0) {
            sum += ~~(newspapers / amount) * cost[amount]
            newspapers %= amount
        }
    })
    return +sum.toFixed(2)
}

q = cheapestQuote(40) // 3.85
q
q = cheapestQuote(20) // 1.93
q
q = cheapestQuote(10) // 0.97
q
q = cheapestQuote(5) // 0.49
q
q = cheapestQuote(1) // 0.10
q
q = cheapestQuote(41) // 3.95, '41 newspapers should be priced as 40 bundle and a 1 bundle'
q
q = cheapestQuote(80) // 7.70, '80 newspapers should be priced as two 40 bundles'
q
q = cheapestQuote(26) // 2.52, '26 newspapers should be priced as a 20 bundle, a 5 bundle and a 1 bundle'
q