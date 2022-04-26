package step

/*
fun step(g: Int, m: Long, n: Long): LongArray {
    val prime = (m..n - g).firstOrNull { isPrime(it) and isPrime(it + g) }

    return if (prime == null) longArrayOf() else longArrayOf(prime, prime + g)
}
*/

/*
fun isPrime(n: Long): Boolean {
    if (n == 2L || n == 3L || n == 5L) return true
    if (n < 2L || n % 2 == 0L || n % 3 == 0L || n % 5 == 0L) return false

    for (i in 5..Math.sqrt(n.toDouble()).toLong() step 6)
        if ((n % i == 0L) or (n % (i + 2) == 0L))
            return false

    return true
}
*/

fun step(g: Int, m: Long, n: Long): LongArray {
    return (m..n - g)
        .firstOrNull { isPrime(it) and isPrime(it + g) }
        ?.let {
            longArrayOf(it, it + g)
        } ?: longArrayOf()
}

fun isPrime(n: Long): Boolean = (2..Math.sqrt(n.toDouble()).toLong()).none { n % it == 0L }

/*
fun step(g: Int, m: Long, n: Long): LongArray {
    return (m..n - g).find {
        it.toBigInteger().isProbablePrime(10) and (it + g).toBigInteger().isProbablePrime(10)
    }?.let { longArrayOf(it, it + g) } ?: longArrayOf()
}
*/

