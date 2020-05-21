// 7kyu - Dave's gamble

/* My mate Dave LOVES gambling. He goes to the horse races every Saturday and bets money on 
which horses will finish FIRST, SECOND and THIRD place.

I'm a good friend, so I said I'd help him figure out how many different ways the gold, silver and bronze 
could be handed out to the competitors so he can calculate his odds of winning.

Problem is, Dave never knows how many horses will be entering the race until he gets to the track. 
I guess I'll have to design a funciton to help me!

Write a programme that can take any number of horses as its only argument and returns the total number 
of different combinations of competitors winning gold silver and bronze.

horses(15)  ->  2730
horses(4)  ->  24
horses(1)  ->  1 

There are effectively 2730 different combinations of 1st, 2nd and 3rd finishers.

The function should return undefined if the object entered isn't an integer.
If number of horses is lower than 3, return the input value. */

// function horses(n) {
//     if (isNaN(n) || parseInt(n) != n) return
//     if (n < 3) return n
//     return n * (n - 1) * (n - 2)
// }

// function horses(n) {
//     if (Number.isInteger(n))
//         return n < 3 ? n : n * (n - 1) * (n - 2)
// }

const horses = (n) => Number.isInteger(n) ? n < 3 ? n : n * (n - 1) * (n - 2) : undefined

q = horses(12) // 1320
q
q = horses(15) // 2730, true
q
q = horses(2) // 2
q
q = horses(11) // 5
q
q = horses(2.5) // undefined
q
q = horses("a") // undefined
q