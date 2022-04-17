package newavg

import kotlin.math.roundToLong

/*
fun newAvg(a: DoubleArray, navg: Double): Long {
    val ans = navg * (a.size + 1) - a.sum()

    if (ans < 0)
        throw  IllegalArgumentException("negative answer is invalid")

    return Math.ceil(ans).toLong()
}*/

/*
fun newAvg(a: DoubleArray, navg: Double): Long {
    val ans = navg * (a.size + 1) - a.sum()
    require(ans > 0)

    return Math.ceil(ans).toLong()
}
*/

fun newAvg(a: DoubleArray, navg: Double): Long {
    if (a.average() > navg)
        throw  IllegalArgumentException("avg of $a already greater than $navg")

    return (navg * (a.size + 1) - a.sum()).roundToLong()
}
