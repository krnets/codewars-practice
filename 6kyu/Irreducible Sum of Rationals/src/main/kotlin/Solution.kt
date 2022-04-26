package solution

/*
object SumFractions {
    fun sumFracts(l: Array<IntArray>): String {
        var numer = 0
        var denom = 1

        l.forEach { denom *= it.last() }
        l.forEach { numer += (it.first() * denom / it.last()) }
        val gcd = numer.toBigInteger().gcd(denom.toBigInteger()).toInt()

        return if (l.isEmpty()) "" else if (gcd == denom) "${numer / gcd}" else "[${numer / gcd}, ${denom / gcd}]"
    }
}*/

/*
object SumFractions {
    fun sumFracts(l: Array<IntArray>): String {
        val denom = l.fold(1) { acc, pair -> acc * pair.last() }
        val numer = l.fold(0) { acc, pair -> acc + pair.first() * denom / pair.last() }
        val gcd = numer.toBigInteger().gcd(denom.toBigInteger()).toInt()

        return if (l.isEmpty()) "" else if (gcd == denom) "${numer / gcd}" else "[${numer / gcd}, ${denom / gcd}]"
    }
}
*/

object SumFractions {
    fun sumFracts(l: Array<IntArray>): String {
        val denom = l.fold(1L) { acc, pair -> acc * pair.last() }
        val numer = l.fold(0L) { acc, pair -> acc + pair.first() * denom / pair.last() }
        val gcd = numer.toBigInteger().gcd(denom.toBigInteger()).toLong()

        return if (l.isEmpty()) "" else if (gcd == denom) "${numer / gcd}" else "[${numer / gcd}, ${denom / gcd}]"
    }
}
