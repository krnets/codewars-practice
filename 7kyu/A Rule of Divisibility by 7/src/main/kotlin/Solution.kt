package divseven

fun seven(n: Long): LongArray {
    var count = 0L
    var m = n

    while (m > 99) {
        val x = m / 10
        val y = 2 * (m.mod(10))
        m = x - y
        ++count
    }
    return longArrayOf(m, count)
}