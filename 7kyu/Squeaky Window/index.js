// 7kyu - Squeaky Window

function sliding(nums, k) {
    let result = []

    for (let i = 0; i < Math.max(1, nums.length - k + 1); i++)
        result.push(Math.max(...nums.slice(i, k + i)))

    return result.filter(Number.isFinite)
}
// return result.includes(-Infinity) ? [] : result
// for (let i = 0; i <= nums.length - k; i++) 

q = sliding([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]
q
q = sliding([-7, -8, 7, 5, 7, 1, 6, 0], 4), [7, 7, 7, 7, 7]
q
q = sliding([7, 2, 4], 2), [7, 4]
q
q = sliding([9, 11], 2), [11]
q
q = sliding([9, 11, 12], 1), [9, 11, 12]
q
q = sliding([], 1), []
q
q = sliding([], 50), []
q