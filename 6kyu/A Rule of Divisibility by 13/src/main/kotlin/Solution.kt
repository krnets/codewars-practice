package thirteen

/*
fun thirt(n: Long): Long {
    val pattern = listOf(1, 10, 9, 12, 3, 4)
    var sum = 0L
    var m = n
    var i = 0

    while (m > 0) {
        sum += (m % 10) * pattern[i % pattern.size]
        m /= 10
        i++
    }
    return if (sum == n) sum else thirt(sum)
}
*/

val pattern = intArrayOf(1, 10, 9, 12, 3, 4)

/*
fun thirt(n: Long): Long {
    val p = n.toString()
        .reversed()
        .mapIndexed { index, c ->
            c.digitToInt() * pattern[index % pattern.size]
        }
        .sum().toLong()

    return if (n == p) p else thirt(p)
}
*/

fun thirt(n: Long): Long = n.toString()
    .reversed()
    .mapIndexed { index, c ->
        c.digitToInt() * pattern[index % pattern.size]
    }
    .sum().toLong()
    .let { if (n == it) it else thirt(it) }

/*
fun thirt(n: Long): Long = n.toString()
    .reversed()
    .map { it.digitToInt() }
    .chunked(6) { it.zip(listOf(1, 10, 9, 12, 3, 4)) }
    .flatten()
    .sumOf { it.first * it.second }
    .toLong()
    .let { if (n == it) it else thirt(it) }
*/
