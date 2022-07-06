package kprimessteps

fun kprimesStep(k: Int, step: Int, start: Long, end: Long): List<LongArray> {
    return (start..end - step)
        .filter { countPrimeFactors(it) == k && countPrimeFactors(it + step) == k }
        .map { longArrayOf(it, it + step) }
}

fun countPrimeFactors(m: Long): Int {
    var primeFactors = 0
    var n = m

    while (n % 2 == 0L && n > 0) {
        n /= 2
        primeFactors++
    }

    for (i in 3..Math.sqrt(n.toDouble()).toInt() step 2) {
        while (n % i == 0L) {
            n /= i
            primeFactors++
        }
    }

    return if (n == 1L) primeFactors else primeFactors + 1
}
