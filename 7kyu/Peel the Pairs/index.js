// 7kyu - Peel the Pairs

/* Given a string of numbers and a number n, peel away the pairs of digits that add up to n (starting from index 0). 
The numbers in the pair don't have to be adjacent to each other, but they should be paired with the closest digit 
to the right of them that sums to n.

Return the new string with those pairs removed. */

// function peelPairs(str, n) {
//     let digits = [...str].map(Number)
//     for (let i = 0; i < str.length; i++)
//         for (let j = i + 1; j < str.length; j++)
//             if (digits[i] + digits[j] == n) {
//                 digits.splice(j, 1)
//                 digits.splice(i--, 1)
//             }
//     return digits.join('')
// }

function peelPairs(str, n) {
    let digits = [...str].map(Number)
    for (let i = 0; i < str.length; i++)
        for (let j = i + 1; j < str.length; j++)
            if (digits[i] + digits[j] == n)
                return peelPairs(str.replace(digits[i], '').replace(digits[j], ''), n)
    return str
}


q = peelPairs('14642', 3) // '464'
q
q = peelPairs('732374', 6) // '77'
q
q = peelPairs('245638363', 10) // '53363'
q