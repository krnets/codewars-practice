package solution

import java.math.BigInteger

/*
object SumFct {
    fun perimeter(n: Int): BigInteger = 4.toBigInteger() * sumFibonacci(n)

    fun sumFibonacci(n: Int): BigInteger {
        var sum = BigInteger.ZERO
        var a = BigInteger.ONE
        var b = BigInteger.ONE

        repeat(n + 1) {
            sum += a
            a = b.also { b += a }
        }

        return sum
    }
}*/

object SumFct {
    fun perimeter(n: Int): BigInteger {
        var a = BigInteger.ONE
        var b = BigInteger.ONE

        repeat(n + 2) {
            a = b.also { b += a }
        }

        return 4.toBigInteger() * (a - BigInteger.ONE)
    }
}

/*
object SumFct {
    fun perimeter(n: Int): BigInteger =
        generateSequence(BigInteger.ONE to BigInteger.ONE) { (a, b) -> b to a.plus(b) }
            .map { it.first }
            .take(n + 1)
            .fold(BigInteger.ZERO) { acc, bigInt -> acc + bigInt }
            .multiply(4.toBigInteger())
}
*/
