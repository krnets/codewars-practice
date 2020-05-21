// 7kyu - Sorted? yes? no? how?

/* Complete the method which accepts an array of integers, and returns one of the following:

    "yes, ascending" - if the numbers in the array are sorted in an ascending order
    "yes, descending" - if the numbers in the array are sorted in a descending order
    "no" - otherwise

You can assume the array will always be valid, and there will always be one correct answer.
Fundamentals | Arrays | Sorting |Algorithms */

// const isSortedAndHow = (array) => array.every((_, i) => i == 0 || array[i] >= array[i - 1]) ? 'yes, ascending' :
//     array.every((_, i) => i == 0 || array[i] <= array[i - 1]) ? 'yes, descending' : 'no'

function isSortedAndHow(array) {
    let arr = Array.from(new Set(array))
    let asc = 0;
    let des = 0;
    for (let i = 1; i < arr.length; i++) {
        if (arr[i - 1] < arr[i])
            asc++;
        else if (arr[i - 1] > arr[i])
            des++;
    }
    return asc == arr.length - 1 ? 'yes, ascending' :
           des == arr.length - 1 ? 'yes, descending' : 'no';
}


q = isSortedAndHow([1, 2]) // 'yes, ascending'
q
q = isSortedAndHow([15, 7, 3, -8]) // 'yes, descending'
q
q = isSortedAndHow([4, 2, 30]) // 'no'
q