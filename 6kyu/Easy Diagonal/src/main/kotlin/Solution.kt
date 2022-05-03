package solution

import java.math.BigInteger

/*
object Diagonal {
    fun diagonal(n: Int, p: Int): BigInteger = binomial((n + 1).toBigInteger(), (p + 1).toBigInteger())

    fun binomial(n: BigInteger, k: BigInteger): BigInteger = when {
        k == BigInteger.ZERO -> BigInteger.ONE
        k > (n / BigInteger.TWO) -> binomial(n, n - k)
        else -> n * binomial(n - BigInteger.ONE, k - BigInteger.ONE) / k
    }
}
*/

object Diagonal {
    fun diagonal(n: Int, p: Int): BigInteger = binomial((n + 1).toBigInteger(), (p + 1).toBigInteger())

    fun binomial(n: BigInteger, k: BigInteger): BigInteger = when {
        k == (0).toBigInteger() -> (1).toBigInteger()
        k >= n / (2).toBigInteger() -> binomial(n, n - k)
        else -> n * binomial(n - (1).toBigInteger(), k - (1).toBigInteger()) / k
    }
}
