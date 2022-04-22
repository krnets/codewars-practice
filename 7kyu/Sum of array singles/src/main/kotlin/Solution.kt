/*
fun repeats(arr: IntArray): Int = arr.groupBy { it }
    .entries
    .filter { it.value.size == 1 }
    .sumOf { it.key }*/

fun repeats(arr: IntArray): Int = arr.groupBy { it }
    .filterValues { it.size == 1 }
    .keys
    .sum()
