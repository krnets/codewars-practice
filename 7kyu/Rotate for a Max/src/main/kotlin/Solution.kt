package maxrot

import kotlin.math.max

/*
fun maxRot(n: Long): Long {
    var numStr = n.toString()
    var ans = n.toDouble()

    (0 until numStr.length - 1).forEach { i ->
        val a = numStr.substring(0, i)
        val b = numStr[i]
        val c = numStr.substring(i + 1)
        numStr = "$a$c$b"
        ans = max(ans, numStr.toDouble())
    }
    return ans.toLong()
}*/

fun maxRot(n: Long): Long {
    var digits = n.toString()
    var ans = n

    for (i in digits.indices) {
        digits = StringBuilder(digits + digits[i]).deleteCharAt(i).toString()
        ans = max(ans, digits.toLong())
    }
    return ans
}
