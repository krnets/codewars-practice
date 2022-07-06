package kprimes

fun countKprimes(k: Int, start: Long, end: Long): LongArray {
    return (start..end)
        .filter { countPrimeFactors(it) == k }
        .toLongArray()
}

fun countPrimeFactors(m: Long): Int {
    var primeFactors = 0
    var n = m

    while (n % 2 == 0L && n > 0) {
        n /= 2
        primeFactors++
    }
    val limit = Math.sqrt(n.toDouble()).toInt()

    for (i in 3..limit step 2) {
        while (n % i == 0L) {
            n /= i
            primeFactors++
        }
    }
    return if (n == 1L) primeFactors else primeFactors + 1
}

fun puzzle(s: Int): Int {
    val end = s.toLong()
    var ans = 0

    for (a in countKprimes(1, 2, end))
        for (b in countKprimes(3, 8, end))
            for (c in countKprimes(7, 128, end))
                if (a + b + c == end)
                    ans++
    return ans
}
