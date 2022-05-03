package catKataPartOne

fun peacefulYard(yard: Array<String>, minDistance: Int): Boolean {
    val list = mutableListOf<Pair<Int, Int>>()

    yard.forEachIndexed { i, row ->
        row.forEachIndexed { j, col ->
            if (col != '-')
                list.add(Pair(i, j))
        }
    }
    return when (list.size) {
        0 -> true
        1 -> true
        2 -> distance(list[0], list[1]) >= minDistance
        3 -> listOf(
            distance(list[0], list[1]),
            distance(list[0], list[2]),
            distance(list[1], list[2])
        ).all { it >= minDistance }
        else -> false
    }
}

fun distance(pairA: Pair<Int, Int>, pairB: Pair<Int, Int>): Double =
    kotlin.math.hypot((pairA.first - pairB.first).toDouble(), (pairA.second - pairB.second).toDouble())

//    sqrt(pow((pairA.first - pairB.first).toDouble(), 2.0) + pow((pairA.second - pairB.second).toDouble(), 2.0))
//    hypot(abs(pairA.first - pairB.first).toDouble(), abs(pairA.second - pairB.second).toDouble())
