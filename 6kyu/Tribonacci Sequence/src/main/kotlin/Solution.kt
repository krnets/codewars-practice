/*
fun tribonacci(signature: DoubleArray, n: Int): DoubleArray {
    val arr = DoubleArray(n)
    signature.copyInto(arr, 0, 0)
    var sum = arr[0] + arr[1]

    (3 until n).forEach { i ->
        sum += arr[i - 1]
        arr[i] = sum
        sum -= arr[i - 3]
    }
    return arr
}
*/

/*
fun tribonacci(signature: DoubleArray, n: Int): DoubleArray =
    generateSequence(Triple(signature[0], signature[1], signature[2])) {
        Triple(it.second, it.third, it.first + it.second + it.third)
    }
        .map { it.first }
        .take(n)
        .toList().toDoubleArray()
*/
/*
fun tribonacci(signature: DoubleArray, n: Int): DoubleArray =
    signature.toMutableList().apply {
        repeat(n) {
            add(takeLast(3).sum())
        }
    }.take(n).toDoubleArray()*/

/*
fun tribonacci(signature: DoubleArray, n: Int) = DoubleArray(n).also {
    for (i in 0 until n) {
        if (i < 3)
            it[i] = signature[i]
        else it[i] = it[i - 1] + it[i - 2] + it[i - 3]
    }
}
*/

fun tribonacci(signature: DoubleArray, n: Int): DoubleArray {
    val arr = signature.copyOf(n)

    for (i in 3 until n)
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

    return arr
}
