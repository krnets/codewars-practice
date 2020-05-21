// 6kyu - n times 2 to the power of x

/* You are given a function puzzle that accepts 2 positive integers (very important!) in the specified order, 
n and x, and returns the result of n * Math.pow(2, x). Sounds easy, right? Well, there is only one condition - 
you must shorten the code so it meets the strict (compiled) character count requirements [11 max]
(without altering how the function behaves for positive integers of course). */

// const puzzle=(n,x)=>n*Math.pow(2,x)
let puzzle=(n,x)=>n<<x

q = puzzle(1, 1) // 2
q
q = puzzle(3, 4) // 48
q
q = puzzle(4, 3) // 32
q
q = puzzle(7, 9) // 3584
q
q = puzzle(9, 7) // 1152
q
q = puzzle(13, 16) // 851968
q
q = puzzle(16, 13) // 131072
q