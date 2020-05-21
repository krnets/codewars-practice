// 7kyu - Highest and Lowest

function highAndLow(str) {
    arr = str.split(' ').map(x => parseInt(x))
    let min = arr[0]
    let max = arr[0]

    for (let i = 0; i < arr.length; i++) {
        if (min > arr[i])
            min = arr[i]
        if (max < arr[i])
            max = arr[i]
    }
    return ([max, min]).join(' ')
}


q = highAndLow("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6") // "542 -214"
q