/*
object Kata {
    fun digitize(n: Long): IntArray {
        var digits = mutableListOf<Int>()
        var x = n

        while (x > 0) {
            digits.add((x % 10).toInt())
            x /= 10
        }
        return if (digits.isEmpty()) IntArray(1) else digits.toIntArray()
    }
}*/

object Kata {
    fun digitize(n: Long): IntArray {
        return n.toString().reversed().map { it.digitToInt() }.toIntArray()
    }
}
