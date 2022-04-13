package maxlendiff

/*
fun mxdiflg(a1: Array<String>, a2: Array<String>): Int {
    if (a1.isEmpty() || a2.isEmpty()) return -1

    var minLen1 = Int.MAX_VALUE
    var minLen2 = minLen1
    var maxLen1 = Int.MIN_VALUE
    var maxLen2 = maxLen1

    a1.forEach {
        minLen1 = min(minLen1, it.length)
        maxLen1 = max(maxLen1, it.length)
    }
    a2.forEach {
        minLen2 = min(minLen2, it.length)
        maxLen2 = max(maxLen2, it.length)
    }
    var resA = maxLen1 - minLen2
    var resB = maxLen2 - minLen1

    return max(resA, resB)
}
*/

/*
fun mxdiflg(a1: Array<String>, a2: Array<String>): Int {
    if (a1.isEmpty() || a2.isEmpty()) return -1

    var statsA1 = a1.toList().stream().mapToInt { it.length }.summaryStatistics()
    var statsA2 = a2.toList().stream().mapToInt { it.length }.summaryStatistics()

    var resA = statsA1.max - statsA2.min
    var resB = statsA2.max - statsA1.min

    return max(resA, resB)
}
*/

fun mxdiflg(a1: Array<String>, a2: Array<String>): Int {
    if (a1.isEmpty() || a2.isEmpty()) return -1

    var res1 = a1.maxOf { it.length } - a2.minOf { it.length }
    var res2 = a2.maxOf { it.length } - a1.minOf { it.length }

    return Math.max(res1, res2)
}
