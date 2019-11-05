// 6kyu - Sort two arrays [incomplete]

function isAscending(arr) {
    for (let i = 1; i < arr.length; i++) 
        if (arr[i] < arr[i-1]) 
            return false
    return true
}

function sortArrays(arr1, arr2) {
    let a = isAscending(arr2)
    a

}


// q = isAscending([5,4,3,2,1])
// q
// q = isAscending([6,5,7,8,9])
// q
// q = isAscending([5,5,7,8,9])
// q
// q = isAscending([5,6,7,8,9])
// q

q = sortArrays([5,4,3,2,1],[6,5,7,8,9]) // [[4,5,3,2,1],[9,8,7,5,6]])
q
// q = sortArrays([2,1,3,4,5],[5,6,7,8,9]) // [[2,1,3,4,5],[6,5,7,8,9]])
// q
// q = sortArrays([5,6,9,2,6,5],[3,6,7,4,8,1]) // [[5,5,2,6,9,6],[4,3,1,6,8,7]])
// q