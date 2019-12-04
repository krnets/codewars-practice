// 7kyu - Find Count of Most Frequent Item in an Array

/* Complete the function to find the count of the most frequent item of an array. 
You can assume that input is an array of integers. For an empty array return 0

input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5 

The most frequent number in the array is -1 and it occurs 5 times. */

function mostFrequentItemCount(collection) {
    let count = new Map()
    collection.forEach(v => count[v] = ++count[v] || 1)
    return collection.length && Object.entries(count).sort((a, b) => b[1] - a[1])[0][1]
}

// import _ from 'lodash';
// const mostFrequentItemCount = collection => collection.length && _(collection).countBy().values().max().valueOf() 
// const mostFrequentItemCount = collection => collection.length && _(collection).countBy().values().max()


let q = mostFrequentItemCount([3, -1, -1]) // 2
q
q = mostFrequentItemCount([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]) // 5
q