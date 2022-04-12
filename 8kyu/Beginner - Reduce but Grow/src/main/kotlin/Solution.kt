package reducebutgrow

fun grow(arr: IntArray): Int = arr.reduce { acc, elem -> acc * elem }
