// 6kyu - Find number in an array # 5


function countNumber(arr, num) {
    let count = 0
    for (let i = 0; i < arr.length; i++) {
        let start = 0
        let end = arr[i].length - 1
        while (start <= end) {
            let mid = ((start + end) >> 1)
            if (arr[i][mid] === num) {
                count++
                break
            } else if (arr[i][mid] < num)
                start = mid + 1
            else
                end = mid - 1
        }
    }
    return count
}

q = countNumber([
    [1, 3, 5, 7],
    [2, 4, 7, 8],
    [3, 5, 9, 10]
], 3) // 2
q

q = countNumber([
    [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81],
    [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82],
    [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83],
    [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
    [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]
], 81) // 5
q

const binarySearch = function (arr, x) {
    let start = 0,
        end = arr.length - 1;
    // Iterate while start not meets end 
    while (start <= end) {

        // Find the mid index 
        let mid = Math.floor((start + end) / 2);

        // If element is present at mid, return True 
        if (arr[mid] === x) return true;

        // Else look in left or right half accordingly 
        else if (arr[mid] < x)
            start = mid + 1;
        else
            end = mid - 1;
    }
    return false;
}

q = binarySearch([1, 3, 5, 7], 3) // 2
q