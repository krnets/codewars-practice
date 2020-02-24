// 6kyu - Delete occurrences of an element if it occurs more than n times

/* Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, 
and now they want to show Charlie their entire collection. However, Charlie doesn't like this sessions, 
since the motive usually repeats. He isn't fond of seeing the Eiffel tower 40 times. 
He tells them that he will only sit during the session if they show the same motive at most N times. 
Luckily, Alice and Bob are able to encode the motive as a number. Can you help them to remove numbers 
such that their list contains each number only up to N times, without changing the order?

Given a list lst and a number N, create a new list that contains each number of lst at most N times 
without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, 
which leads to [1,2,3,1,2,3]. */

// function deleteNth(arr, n) {
//     let freq = arr.reduce((count, v) => {
//         if (!count[v]) count[v] = 1;
//         else if (count[v] == n);
//         else count[v] = ++count[v];
//         return count; }, {})
//     let res = [];
//     for (let v of arr) {
//         if (freq[v] > 0) {
//             res.push(v);
//             freq[v]--;
//         }
//     }
//     return res;
// }

// const deleteNth = (arr, n, freq = {}) => arr.filter(v => (freq[v] = ++freq[v] || 1, freq[v] <= n))
const deleteNth = (arr, n) => arr.filter((v, i) => arr.slice(0, i).filter(p => v == p).length < n)


q = deleteNth([1, 1, 1, 1], 2) // return [1,1]
q
q = deleteNth([20, 37, 20, 21], 1) // return [20,37,21]
q
q = deleteNth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) // [1, 1, 3, 3, 7, 2, 2, 2]
q