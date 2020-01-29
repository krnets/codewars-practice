// 7kyu - Christmas baubles on the tree

/* You've came to visit your grandma and she straight away found you a job - her Christmas tree needs decorating!
She first shows you a tree with an identified number of branches, and then hands you a some baubles (or loads of them!).
You know your grandma is a very particular person and she would like the baubles to be distributed in the orderly manner. 
You decide the best course of action would be to put the same number of baubles on each of the branches (if possible) 
or add one more bauble to some of the branches - starting from the beginning of the tree.
In this kata you will return an array of baubles on each of the branches.

10 baubles, 2 branches: [5,5] 5 baubles, 7 branches: [1,1,1,1,1,0,0] 12 baubles, 5 branches: [3,3,2,2,2]

The numbers of branches and baubles will be always greater or equal to 0. 
If there are 0 branches return: "Grandma, we will have to buy a Christmas tree first!". */

// function baublesOnTree(baubles, branches) {
//     let bauble = Math.floor(baubles / branches)
//     let xmasTree = Array(branches).fill(bauble)
//     for (let i = 0; i < xmasTree.length; i++)
//         if (baubles > xmasTree.reduce((a, b) => a + b, 0))
//             xmasTree[i]++
//     return branches > 0 ? xmasTree : "Grandma, we will have to buy a Christmas tree first!"
// }

function baublesOnTree(baubles, branches) {
    for (var xmasTree = [], i = 0; i < branches; i++)
        xmasTree.push(Math.floor(baubles / branches) + (i < baubles % branches ? 1 : 0))
    return branches > 0 ? xmasTree : "Grandma, we will have to buy a Christmas tree first!"
}

q = baublesOnTree(26, 1)
q
q = baublesOnTree(5, 5) // [1,1,1,1,1]
q
q = baublesOnTree(5, 0) // "Grandma, we will have to buy a Christmas tree first!"
q
q = baublesOnTree(6, 5) // [2,1,1,1,1]
q
q = baublesOnTree(50, 9) // [6,6,6,6,6,5,5,5,5]
q
q = baublesOnTree(20, 4) // [5,5,5,5]
q
q = baublesOnTree(0, 10) // [0,0,0,0,0,0,0,0,0,0]
q