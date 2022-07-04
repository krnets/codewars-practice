/*
val adjacentKeyMap = mapOf(
    0 to "8", 1 to "24", 2 to "135", 3 to "26", 4 to "157",
    5 to "2468", 6 to "359", 7 to "48", 8 to "0579", 9 to "68"
)

fun getPINs(observed: String): List<String> = getCombinations((listOf(observed).toSet()), 0).toList()

fun getCombinations(pins: Set<String>, idx: Int): Set<String> {

    val comboSet = mutableSetOf<String>()
    var size = 0

    for (pin in pins) {

        comboSet.add(pin)
        size = pin.length

        val currentKey = pin[idx].digitToInt()
        val adjacentKeys = adjacentKeyMap[currentKey]!!

        for (key in adjacentKeys) {

            val pb = StringBuilder(pin)
            comboSet.add(pb.replace(idx, idx + 1, "$key").toString())
        }
    }

    if (idx == size - 1)
        return comboSet

    return getCombinations(comboSet, idx + 1)
}*/

/*
val adjacentKeyMap = mapOf(
    '0' to "8", '1' to "24", '2' to "135", '3' to "26", '4' to "157",
    '5' to "2468", '6' to "359", '7' to "48", '8' to "0579", '9' to "68"
)

fun getPINs(observed: String): List<String> = getCombinations((listOf(observed).toSet()), 0).toList()

fun getCombinations(pins: Set<String>, idx: Int): Set<String> {

    val comboSet = mutableSetOf<String>()
    var size = 0

    for (pin in pins) {

        comboSet.add(pin)
        size = pin.length
        val currentKey = pin[idx]

        for (adjacentKey in adjacentKeyMap[currentKey]!!) {

            val sb = StringBuilder(pin)
            comboSet.add(sb.replace(idx, idx + 1, "$adjacentKey").toString())
        }
    }

    if (idx == size - 1)
        return comboSet

    return getCombinations(comboSet, idx + 1)
}
*/

/*
fun padLock(touched: Char) = when (touched) {
    '1' -> listOf(1, 2, 4)
    '2' -> listOf(1, 2, 3, 5)
    '3' -> listOf(2, 3, 6)
    '4' -> listOf(1, 4, 5, 7)
    '5' -> listOf(2, 4, 5, 6, 8)
    '6' -> listOf(3, 5, 6, 9)
    '7' -> listOf(4, 7, 8)
    '8' -> listOf(5, 7, 8, 9, 0)
    '9' -> listOf(6, 8, 9)
    '0' -> listOf(8, 0)
    else -> error("touched $touched")
}.map { it.toString() }


fun getPINs(observed: String): List<String> = observed
    .map { padLock(it) }
    .reduce { acc, pins -> pins.flatMap { a -> acc.map { it + a } } }
    .distinct()

*/

val adjacentKeys = mapOf(
    '1' to "124", '2' to "1235", '3' to "236", '4' to "1457", '5' to "24568",
    '6' to "3569", '7' to "478", '8' to "57890", '9' to "689", '0' to "80"
)

fun getPINs(observed: String): List<String> =
    observed.map { adjacentKeys[it]!!.map { key -> "$key" } }
        .reduce { acc, pin -> pin.flatMap { adjacent -> acc.map { it + adjacent } } }
