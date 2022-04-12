package bouncing

import kotlin.math.*

/*
fun bouncingBall(h: Double, bounce: Double, window: Double): Int {
    if (h <= 0 || bounce <= 0 || bounce >= 1 || window >= h) return -1

    var count = 0
    var ballPos = h

    while (ballPos > window) {
        ++count
        ballPos *= bounce
    }
    return 2 * count - 1
}*/

/*
fun bouncingBall(h: Double, bounce: Double, window: Double): Int {
    if (h <= 0 || bounce <= 0 || bounce >= 1 || window >= h) return -1

    var count = -1
    var ballPos = h

    while (ballPos > window) {
        count += 2
        ballPos *= bounce
    }
    return count
}
*/

/*
fun bouncingBall(h: Double, bounce: Double, window: Double): Int {
    if (h <= 0 || bounce <= 0 || bounce >= 1 || window >= h) return -1

    return generateSequence(h) { it * bounce }
        .takeWhile { it > window }
        .count() * 2 - 1
}
*/

fun bouncingBall(h: Double, bounce: Double, window: Double): Int {
    return ceil(log(window / h, bounce)).toInt() * 2 - 1
}
