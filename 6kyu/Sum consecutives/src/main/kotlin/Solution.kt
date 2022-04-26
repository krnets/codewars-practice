/*
fun sumConsecutives(s: List<Int>): List<Int> {
    val res = mutableListOf<Int>()
    var prev = s.first()
    var sum = prev

    (1..s.lastIndex).forEach { i ->
        if (s[i] == prev) {
            sum += prev
        } else {
            res.add(sum)
            prev = s[i]
            sum = prev
        }
    }
    return res + sum
}*/

/*
fun sumConsecutives(s: List<Int>): List<Int> {
    val res = mutableListOf<Int>()
    var prev: Int? = null

    s.forEach {
        if (it == prev) res[res.lastIndex] += it
        else res.add(it)
        prev = it
    }
    return res
}
*/

/*
fun sumConsecutives(s: List<Int>): List<Int> =
    if (s.isEmpty()) s
    else s.takeWhile { it == s.first() }
        .let {
            listOf(it.sum()) + sumConsecutives(s.drop(it.size))
        }
*/

fun sumConsecutives(s: List<Int>): List<Int> =
    if (s.size <= 1) s
    else sumConsecutives(s.dropLastWhile { it == s.last() }) + s.takeLastWhile { it == s.last() }.sum()

