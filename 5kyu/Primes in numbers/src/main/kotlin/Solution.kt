package solution

/*
object PrimeDecomp {
    fun factors(l: Int): String {
        val list = mutableListOf<Int>()
        var divisor = 2
        var n = l

        while (n != 1) {

            while (n % divisor == 0) {
                n /= divisor
                list.add(divisor)
            }
            divisor++
        }

        return list.groupBy { it }
            .map {
                if (it.value.size > 1) "(${it.key}**${it.value.size})"
                else "(${it.key})"
            }
            .joinToString("")
    }
}*/

object PrimeDecomp {
    fun factors(l: Int): String {
        val primeDivCount = mutableMapOf<Int, Int>()
        var divisor = 2
        var n = l

        while (n > 1) {

            while (n % divisor == 0) {
                n /= divisor
                primeDivCount.merge(divisor, 1, Int::plus)
            }
            divisor++
        }

        return primeDivCount.map { (k, v) ->
            if (v > 1) "(${k}**${v})"
            else "(${k})"
        }.joinToString("")
    }
}
