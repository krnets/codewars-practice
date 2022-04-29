package cycle

import java.math.BigInteger

/*
fun cycle(n: Int): Int {
    if (n % 2 == 0 || n % 5 == 0)
        return -1

    val power10 = BigInteger.valueOf(10L)
    val m = BigInteger.valueOf(n.toLong())
    var exponent = 1L

    while (power10.modPow(BigInteger.valueOf(exponent), m) != BigInteger.ONE)
        exponent++

    return exponent.toInt()
}
*/

fun cycle(n: Int): Int {
    if (n % 2 == 0 || n % 5 == 0) return -1

    var m = 10 % n
    var ans = 1

    while (m != 1) {
        var x = m * 10
        m = x % n
        ans++
    }
    return ans
}
