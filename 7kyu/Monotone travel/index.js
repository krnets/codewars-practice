// 7kyu - Monotone travel

/* Peter lives on a hill, and he always moans about the way to his home. "It's always just up. I never get a rest". 
But you're pretty sure that at least at one point Peter's altitude doesn't rise, but fall. To get him, you use a nefarious plan: 
you attach an altimeter to his backpack and you read the data from his way back at the next day.

You're given a list of compareable elements:

heights = [h1, h2, h3, …, hn]

Your job is to check whether for any x all successors are greater or equal to x.

isMonotone([1,2,3]) == true
isMonotone([1,1,2]) == true
isMonotone([1])     == true
isMonotone([3,2,1]) == false
isMonotone([3,2,2]) == false

If the list is empty, Peter has probably removed your altimeter, so we cannot prove him wrong and he's still right:

isMonotone([])     == True

Such a sequence is also called monotone or monotonic sequence, hence the name isMonotone. */

const range = (a, b, step = b - a > 0 ? 1 : -1) => Array(Math.abs(a - b) + 1).fill().map((_, i) => Math.abs(a * step + i))

// function range(a, b) {
//     let res = []
//     let step = b - a > 0 ? 1 : -1
//     do {
//         res.push(a)
//     } while (step * (b - (a += step)) >= 0)
//     return res;
// };

const isMonotone = (arr) => arr.every((v, i) => !i || v >= arr[i - 1])
// const isMonotone = (arr) => !arr.some((v, i) => v > arr[i + 1])

// q = range(5,1)
// q
// q = range(1, 10)
// q
q = isMonotone(range(1, 10)) // true
q
q = isMonotone(range(4, 12)) // true
q
q = isMonotone([5, 5, 5, 5, 5]) // true
q
q = isMonotone([]) // true
q
q = isMonotone(range(5, 1)) // false
q
q = isMonotone([1, 2, 3, 3, 4, 5]) // true
q