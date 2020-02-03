// 7kyu - Help the Fruit Guy

/* Our fruit guy has a bag of fruit (represented as an array of strings) where some fruits are rotten. 
He wants to replace all the rotten pieces of fruit with fresh ones. 
For example, given ["apple","rottenBanana","apple"] the replaced array should be ["apple","banana","apple"]. 

Your task is to implement a method that accepts an array of strings containing fruits should 
returns an array of strings where all the rotten fruits are replaced by good ones.

    If the array is null/nil/None or empty you should return empty array ([]).
    The rotten fruit name will be in this camelcase (rottenFruit).
    The returned array should be in lowercase. */

// function removeRotten(bagOfFruits) {
//     return bagOfFruits ? bagOfFruits.map(v => /^rotten/.test(v) ? v.toLowerCase().replace(/^rotten/, '') : v) : []
// }

// const removeRotten = (bagOfFruits) => (bagOfFruits || []).map(fruit => /^rotten/.test(fruit) ? fruit.toLowerCase().replace(/^rotten/, '') : fruit)
const removeRotten = (bagOfFruits) => (bagOfFruits || []).map(fruit => fruit.includes('rotten') ? fruit.slice(6).toLowerCase() : fruit)

q = removeRotten(["apple", "rottenBanana", "apple"]) // ["apple","banana","apple"]
q
q = removeRotten(["apple", "banana", "kiwi", "melone", "orange"]) // ["apple","banana","kiwi","melone","orange"]
q
q = removeRotten([]) // []
q