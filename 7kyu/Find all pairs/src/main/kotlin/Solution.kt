/*
fun duplicates(array: IntArray): Int = array.asSequence()
    .groupingBy { it }
    .eachCount()
    .map { it.value / 2 }
    .sum()
*/

fun duplicates(array: IntArray): Int = array
    .groupBy { it }
    .map { it.value.size / 2 }
    .sum()

/*
fun duplicates(array: IntArray): Int = array
    .groupBy { it }
    .values
    .sumOf { it.size / 2 }
*/
