package easyline

import java.math.BigInteger;

/*
fun easyLine(n: Int): BigInteger {
    return choose(BigInteger.valueOf((2 * n).toLong()), BigInteger.valueOf(n.toLong()))
}

fun choose(n: BigInteger, k: BigInteger): BigInteger {
    return factorial(n).divide(factorial(k).times(factorial(n.minus(k))))
}

fun factorial(n: BigInteger): BigInteger {
    return if (n == BigInteger.ZERO) BigInteger.ONE else n.times(factorial(n.minus(BigInteger.ONE)))
}*/

fun easyLine(n: Int): BigInteger {
    var ans = BigInteger.ONE
    val N = BigInteger.valueOf((2 * n).toLong())

    repeat(n) {
        ans = ans.multiply(
            N.minus(BigInteger.valueOf(it.toLong()))
        ).divide(BigInteger.valueOf((it + 1).toLong()))
    }
    return ans
}
