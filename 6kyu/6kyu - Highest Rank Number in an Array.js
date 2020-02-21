// 6kyu - Highest Rank Number in an Array

/* Complete the method which returns the number which is most frequent in the given input array. 
If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3    */

// function highestRank(arr) {
//     let freq = {}
//     arr.forEach(v => freq[v] = ++freq[v] || 1)
//     let [aa, bb] = Object.entries(freq).sort((a, b) => a[1] - b[1]).slice(-2)
//     return aa == bb ? Math.max(...arr) : +bb[0]
// }

function highestRank(arr) {
    let highest = 0
    let key = 0
    let freq = {}
    arr.forEach(v => freq[v] = ++freq[v] || 1)
    Object.keys(freq).forEach(v => {
        if (freq[v] >= highest) {
            highest = freq[v]
            key = v
        }
    })
    return +key
}

var arr = [12, 10, 8, 12, 7, 6, 4, 10, 12];
q = highestRank(arr) // 12
q