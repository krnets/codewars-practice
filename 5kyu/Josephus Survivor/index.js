// 5kyu - Josephus Survivor

/* In this kata you have to correctly return who is the "survivor", ie: the last element of a Josephus permutation.

Basically you have to assume that n people are put into a circle and that they are eliminated in steps of k elements, like this:

josephus_survivor(7,3) => means 7 people in a circle;
one every 3 is eliminated until one remains
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out
[1,2,4,5,7] => 6 is counted out
[1,4,5,7] => 2 is counted out
[1,4,5] => 7 is counted out
[1,4] => 5 is counted out
[4] => 1 counted out, 4 is the last element - the survivor!

The above link about the "base" kata description will give you a more thorough insight about the origin of this kind of permutation, 
but basically that's all that there is to know to solve this kata.

Notes and tips: using the solution to the other kata to check your function may be helpful, but as much larger numbers will be used, 
using an array/list to compute the number of the survivor may be too slow; you may assume that both n and k will always be >=1.
Algorithms | Mathematics | Numbers | Lists | Data Structures | Arrays */

// function josephusSurvivor(n, k) {
//     let arr = Array(n).fill().map((_, i) => i + 1)
//     let i = 0
//     while (arr.length != 1)
//         arr.splice(i = (i + k - 1) % arr.length, 1)
//     return arr[0]
// }

function josephusSurvivor(n, k) {
    let res = 1;
    for (let i = 1; i <= n; i++)
        res = (res + k - 1) % i + 1;
    return res;
}

// const josephusSurvivor = (n, k) => n < 1 ? 1 : (josephusSurvivor(n - 1, k) + --k) % n + 1

q = josephusSurvivor(7, 3) // 4
q
q = josephusSurvivor(11, 19) // 10
q
q = josephusSurvivor(1, 300) // 1
q
q = josephusSurvivor(14, 2) // 13
q
q = josephusSurvivor(100, 1) // 100
q