package gps

/*
fun gps(s: Int, x: DoubleArray): Int = if (x.size <= 1) 0 else x.asSequence()
    .windowed(2)
    .maxOf { 3600 * (it.last() - it.first()) / s }
    .toInt()*/

fun gps(s: Int, x: DoubleArray): Int = x.asSequence()
    .zipWithNext { a, b -> (b - a) * 3600 / s }
    .maxOfOrNull { it }
    ?.toInt() ?: 0
