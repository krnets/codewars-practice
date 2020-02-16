// 5kyu - Weight for weight

/* My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list 
with the weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". 
It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. 
Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"

When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) 
and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 
since, having the same "weight" (9), it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

    it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace 
    between two consecutive numbers
    Don't modify the input
    For C: The result is freed. */

// function orderWeight(string) {
//     let weight = {}
//     string.split(' ').forEach((v, i) => weight[v + '-' + i] = [...v].reduce((a, b) => a + Number(b), 0))
//     return Object.entries(weight).sort((a, b) => a[1] == b[1] ? a[0].localeCompare(b[0]) : a[1] - b[1]).map(v => v[0].replace(/-.*/, '')).join(' ')
// }

const digitSum = n => [...n].reduce((a, b) => a + Number(b), 0)

const orderWeight = string => string.split(' ').sort((a, b) => digitSum(a) - digitSum(b) || a.localeCompare(b)).join(' ')

q = orderWeight("103 123 4444 99 2000") // "2000 103 123 4444 99"
q
q = orderWeight("2000 10003 1234000 44444444 9999 11 11 22 123") // "11 11 2000 10003 22 123 1234000 44444444 9999"
q