/*
fun evaporator(content: Double, evap_per_day: Double, threshold: Double): Int {
    var nthDay = 0
    var contentRemaining = content
    val outOfUse = content * (threshold / 100)
    val reduceBy = (100 - evap_per_day) / 100

    while (contentRemaining >= outOfUse) {
        contentRemaining *= reduceBy
        nthDay++
    }
    return nthDay
}*/

fun evaporator(content: Double, evap_per_day: Double, threshold: Double): Int {
    return generateSequence(content) {
        it - (it * (evap_per_day / 100))
    }
        .takeWhile { it > (content / 100 * threshold) }
        .count()
}
