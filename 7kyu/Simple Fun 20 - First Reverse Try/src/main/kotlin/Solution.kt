/*
fun firstReverseTry(arr: IntArray): IntArray {
    if (arr.isEmpty()) return arr

    val temp = arr.first()
    arr[0] = arr.last()
    arr[arr.lastIndex] = temp

    return arr
}*/

/*
fun firstReverseTry(arr: IntArray): IntArray {
    if (arr.isEmpty()) return arr

    if (arr.first() != arr.last()) {
        arr[0] = arr[0].xor(arr[arr.lastIndex])
        arr[arr.lastIndex] = arr[arr.lastIndex].xor(arr[0])
        arr[0] = arr[0].xor(arr[arr.lastIndex])
    }
    return arr
}
*/

fun firstReverseTry(arr: IntArray): IntArray {
    if (arr.isEmpty()) return arr

    if (arr.first() != arr.last()) {
        arr[0] = arr[0].xor(arr[arr.lastIndex])
        arr[arr.lastIndex] = arr[arr.lastIndex].xor(arr[0])
        arr[0] = arr[0].xor(arr[arr.lastIndex])
    }
    return arr
}

