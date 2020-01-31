// 7kyu - Simple Fun #18: Candles

/* When a candle finishes burning it leaves a leftover. 
makeNew leftovers can be combined to make a new candle, which, when burning down, will in turn leave another leftover.

You have candlesNumber candles in your possession. 
What's the total number of candles you can burn, assuming that you create new candles as soon as you have enough leftovers?

For candlesNumber = 5 and makeNew = 2, the output should be 9.

Here is what you can do to burn 9 candles:

burn 5 candles, obtain 5 leftovers;
create 2 more candles, using 4 leftovers (1 leftover remains);
burn 2 candles, end up with 3 leftovers;
create another candle using 2 leftovers (1 leftover remains);
burn the created candle, which gives another leftover (2 leftovers in total);
create a candle from the remaining leftovers;
burn the last candle.
Thus, you can burn 5 + 2 + 1 + 1 = 9 candles, which is the answer.

    [input] integer candlesNumber
    The number of candles you have in your possession.

    Constraints: 1 ≤ candlesNumber ≤ 50.

    [input] integer makeNew
    The number of leftovers that you can use up to create a new candle.

    Constraints: 2 ≤ makeNew ≤ 5.

    [output] an integer */


// function candles(candlesNumber, makeNew) {
//     let burned = 0
//     let leftovers = 0
//     for (let i = 0; i < candlesNumber; i++) {
//         burned++
//         leftovers++
//         if (leftovers == makeNew) {
//             leftovers -= makeNew
//             i--
//         }
//     }
//     return burned
// }

// function candles(candlesNumber, makeNew, leftOver = 0) {
//     leftOver += candlesNumber
//     if (leftOver < makeNew) return candlesNumber
//     return candlesNumber + candles(~~(leftOver / makeNew), makeNew, leftOver % makeNew)
// }

const candles = (c, m) => Math.ceil(c * (m / (m - 1))) - 1

q = candles(5, 2) //  9
q
q = candles(1, 2) //  1
q
q = candles(3, 3) //  4
q
q = candles(11, 3) // 16
q