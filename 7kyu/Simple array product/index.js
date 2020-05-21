// 7kyu - Simple array product

/* In this Kata, you will be given 2 or more arrays of integers, both positive and negative. 
Your task is to find the maximum product that can be formed by taking one element from each array.

solve([[1, 2],[3, 4]]) = 8, given by 2 * 4
solve([[10,-15],[-1,-3]]) = 45, given by (-15) * (-3)          */

function solve(arr) {
    let maxProduct = -Infinity

    let traverse = function(depth, product) {
        if (depth >= arr.length) {
            if (product > maxProduct) 
                maxProduct = product
            return
        }
        var curLevel = arr[depth]

        for (var i = 0; i < curLevel.length; i++) 
            traverse(depth + 1, product * curLevel[i])
    }
    traverse(0, 1)

    return maxProduct
}

q = solve([ [1, 2], [3, 4] ]) // 8
q
q = solve([[10,-15],[-1,-3]]) // 45
q
q = solve([[-1,2,-3,4],[1,-2,3,-4]]) // 12
q
q = solve([[-11,-6],[-20,-20],[18,-4],[-20, 1]]) // 17600
q
q = solve([[14,2],[0,-16],[-12,-16]]) // 3584
q
q = solve([[-3,-4],[1,2,-3]]) // 12
q
