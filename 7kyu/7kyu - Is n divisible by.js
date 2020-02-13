// 7kyu - Is n divisible by (...)?

/* Create a function isDivisible(n,...) that checks if the first agrument n is divisible by all other arguments 
(return true if no other arguments)

isDivisible(6,1,3)--> true because 6 is divisible by 1 and 3
isDivisible(12,2)--> true because 12 is divisible by 2
isDivisible(100,5,4,10,25,20)--> true
isDivisible(12,7)--> false because 12 is not divisible by 7  */

const isDivisible = (n, ...nums) => nums.every(v => n % v == 0)

q = isDivisible(3, 3, 4) // false
q
q = isDivisible(12, 3, 4) // true
q
q = isDivisible(8, 3, 4, 2, 5) // false
q
