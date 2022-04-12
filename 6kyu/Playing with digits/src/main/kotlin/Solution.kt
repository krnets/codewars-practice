import kotlin.math.pow

/*
fun digPow(n: Int, p: Int): Int {
    var digits = n.toString().map { it.digitToInt().toDouble() }
    var sum = 0

    digits.forEachIndexed { index, x ->
        sum += x.pow(p + index).toInt()
    }
    var k = if (sum % n == 0) sum / n else -1

    return k
}*/

/*
fun digPow(n: Int, p: Int): Int {
    var digits = n.toString().map { it.digitToInt().toDouble() }
    var sum = digits.mapIndexed { index, d -> d.pow(p + index) }.sum().toInt()

    return if (sum % n == 0) sum / n else -1
}
*/

/*
fun digPow(n: Int, p: Int): Int {
    var sum = n.toString()
        .mapIndexed { index, c -> c.digitToInt().toDouble().pow(p + index) }
        .sum().toInt()

    return if (sum % n == 0) sum / n else -1
}
*/

/*
fun digPow(n: Int, p: Int): Int = n.toString()
    .mapIndexed { index, c -> c.digitToInt().toDouble().pow(p + index).toInt() }
    .sum().let {
        if (it % n == 0) it / n else -1
    }
*/

fun digPow(n: Int, p: Int): Int = n.toString()
    .map { it.digitToInt().toDouble() }
    .mapIndexed { index, d -> d.pow(p + index).toInt() }
    .sum().let { if (it % n == 0) it / n else -1 }

/*
fun digPow(n: Int, p: Int): Int = n.toString()
    .map { it.digitToInt().toDouble() }
    .foldIndexed(0.0) { i, acc, d -> acc + d.pow(p + i) }.toInt()
    .let { if (it % n == 0) it / n else -1 }
*/
