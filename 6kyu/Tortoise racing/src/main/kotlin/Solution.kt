package tortoise

fun race(v1: Int, v2: Int, g: Int): IntArray {
    if (v1 >= v2) return intArrayOf()

    val secondsInHour = 60 * 60
    val timeToCatchA = secondsInHour * g / (v2 - v1)
    val hours = timeToCatchA / secondsInHour
    val minutes = timeToCatchA % secondsInHour / 60
    val seconds = timeToCatchA % 60

    return intArrayOf(hours, minutes, seconds)
}