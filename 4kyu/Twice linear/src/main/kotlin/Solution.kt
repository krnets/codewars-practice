package dbllinear

import java.util.LinkedList

/*
fun dblLinear(n: Int): Int {
    var x = 1
    val y = mutableListOf<Int>()
    val z = mutableListOf<Int>()

    repeat(n) {
        y.add(2 * x + 1)
        z.add(3 * x + 1)

        val mn = minOf(y.first(), z.first())

        if (mn == y.first()) {
            x = y.first()
            y.removeFirst()
        }
        if (mn == z.first()) {
            x = z.first()
            z.removeFirst()
        }
    }
    return x
}
*/

fun dblLinear(n: Int): Int {
    var x = 1
    val y = LinkedList<Int>()
    val z = LinkedList<Int>()

    repeat(n) {
        y.add(2 * x + 1)
        z.add(3 * x + 1)

        val mn = minOf(y.first(), z.first())

        if (mn == y.first()) x = y.pop()
        if (mn == z.first()) x = z.pop()
    }
    return x
}
