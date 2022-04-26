package backwards

import java.math.BigInteger

/*
fun backwardsPrime(start: Long, end: Long): String = (start..end)
    .filter { BigInteger.valueOf(it).isProbablePrime(10) }
    .filter { BigInteger.valueOf(it.toString().reversed().toLong()).isProbablePrime(10) }
    .filterNot { it.toString() == it.toString().reversed() }
    .joinToString(" ")*/

fun backwardsPrime(start: Long, end: Long): String = (start..end)
    .filterNot { it.toString() == it.toString().reversed() }
    .filter { isPrime(it) }
    .filter { isPrime(it.toString().reversed().toLong()) }
    .joinToString(" ")

fun isPrime(n: Long) = (2L..Math.sqrt(n.toDouble()).toLong()).none { n % it == 0L }
