package solution

import java.math.BigInteger

/*
object Finance {
    fun finance(n: Int): BigInteger {
        var totalSum = BigInteger.ZERO

        (0..n).forEach { i ->
            totalSum += BigInteger.valueOf((3L * i + n) * (n - i + 1L) / 2)
        }
        return totalSum
    }
}
*/

/*
object Finance {
    fun finance(n: Int): BigInteger = (0L..n)
        .fold(BigInteger.ZERO) { acc, i ->
            acc + BigInteger.valueOf((3 * i + n) * (n - i + 1) / 2)
        }
}
*/

object Finance {
    fun finance(n: Int): BigInteger =
        n.toBigInteger() * (n + 1).toBigInteger() * (n + 2).toBigInteger() / BigInteger.TWO
}


