function maxFall(arr) {
    let recentPeak = 0
    let recentLow = 0
    let largestSoFar = 0
    for (let i = 0; i < arr.length; i++) {
        if (arr[i + 1] != undefined && arr[i] <= arr[i + 1]) { 
            continue
        } else if (arr[i + 1] != undefined && arr[i] > arr[i + 1]) {
            recentPeak = Math.max(arr[i], recentPeak)
            recentLow = Math.min(arr[i + 1], recentPeak)
            if ((recentPeak - recentLow) > largestSoFar) {
                largestSoFar = recentPeak - recentLow
            }
        }
    }
    return +largestSoFar.toFixed(4)
}

// q = maxFall([10, 11, 1, 11, 29, 10])
// q
q = maxFall([10, 11, 1, 11, 29, 10, 14, 20, 5, 1, 10]) // , 28
q
q = maxFall([50, 20, 10, 1, 60, 20, 25]) // , 49
q
q = maxFall([5, 3, 5, 6, 2, 6, 10, 30, 32, 20, 10, 1.1]) // 30.9
q
// q = maxFall([50, 20, 10, 1, 60, 20])
// q