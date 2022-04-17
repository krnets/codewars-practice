package valley

/*
fun makeValley(arr: IntArray): IntArray {
    val left = mutableListOf<Int>()
    val right = mutableListOf<Int>()

    arr.sortedDescending().forEachIndexed { i, x ->
        if (i % 2 == 0)
            left.add(x)
        else right.add(0, x)
    }
    return (left + right).toIntArray()
}*/

fun makeValley(arr: IntArray): IntArray = arr
    .sortedDescending()
    .withIndex()
    .partition { it.index % 2 == 0 }
    .let { pair ->
        pair.first.map { it.value } +
                pair.second.map { it.value }.reversed()
    }.toIntArray()
