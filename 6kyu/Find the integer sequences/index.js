// 6kyu - Find the integer sequences

/* Complete function findSequences. It accepts a positive integer n. Your task is to find such integer sequences:
Continuous positive integer and their sum value equals to n

 For example, n = 15 
 valid integer sequences:
 [1,2,3,4,5]  (1+2+3+4+5==15)
 [4,5,6]          (4+5+6==15)
 [7,8]              (7+8==15)

The result should be an array [sequence 1,sequence 2...sequence n], sorted by ascending order of the length of sequences; 
If no result found, return []. */

function findSequences(n) {
    let res = []
    let range = [...Array(n).keys()]
    for (let i = 1; i < range.length / 2; i++) {
        let sum = 0
        for (let j = i; sum < n; j++) {
            sum += j
            if (sum == n) res.push(range.slice(i, j + 1))
        }
    }
    return res.reverse()
}

q = findSequences(3) // [[1,2]]
q
q = findSequences(15) // [[7,8],[4,5,6],[1,2,3,4,5]]
q
q = findSequences(20) // [[2, 3, 4, 5, 6]]
q
q = findSequences(100) // [[18, 19, 20, 21, 22], [9, 10, 11, 12, 13, 14, 15, 16]]
q
q = findSequences(1) // []
q