package operarray

import java.util.function.LongBinaryOperator

fun gcdi(xx: Long, yy: Long): Long = if (yy == 0L) Math.abs(xx) else gcdi(yy, xx % yy)
fun lcmu(a: Long, b: Long): Long = Math.abs(a * b) / gcdi(a, b)
fun som(a: Long, b: Long): Long = a + b
fun maxi(a: Long, b: Long): Long = if (a > b) a else b
fun mini(a: Long, b: Long): Long = if (a < b) a else b

/*
fun operArray(f: LongBinaryOperator, arr: LongArray, init: Long): LongArray {
    val result = LongArray(arr.size)
    var prev = init

    result.forEachIndexed { i, _ ->
        result[i] = f.applyAsLong(prev, arr[i])
        prev = result[i]
    }
    return result
}
*/

/*
fun operArray(f: LongBinaryOperator, arr: LongArray, init: Long): LongArray {
    val result = LongArray(arr.size)
    var prev = init

    result.indices.forEach { i ->
        result[i] = f.applyAsLong(prev, arr[i])
        prev = result[i]
    }
    return result
}
*/

fun operArray(f: LongBinaryOperator, arr: LongArray, init: Long): LongArray {
    return LongArray(arr.size).apply {
        arr.foldIndexed(init) { index, acc, x ->
            f.applyAsLong(acc, x).also { set(index, it) }
        }
    }
}
