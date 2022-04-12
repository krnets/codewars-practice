package weight

/*
fun orderWeight(string: String): String = string.split(' ')
    .map { Pair(it, weigh(it)) }
    .sortedWith(compareBy<Pair<String, Int>> { it.second }.thenBy { it.first })
    .joinToString(" ") { it.first }

fun weigh(str: String): Int = str.map { it.digitToInt() }.sum()
*/

fun orderWeight(string: String): String = string.split(' ')
    .sortedWith(
        compareBy(
            { it.sumOf { it.digitToInt() } },
            { it })
    ).joinToString(" ")
