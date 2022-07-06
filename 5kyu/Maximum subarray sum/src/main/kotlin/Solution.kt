fun maxSequence(arr: List<Int>): Int {
    var resMaxSum = 0
    var curMaxSum = 0

    for (x in arr) {
        curMaxSum = maxOf(0, curMaxSum + x)
        resMaxSum = maxOf(resMaxSum, curMaxSum)
    }

    return resMaxSum
}