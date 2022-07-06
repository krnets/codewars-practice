package solution

object Suite {
    fun going(n: Int): Double =
        if (n == 0) 0.0
        else 1 + going(n - 1) / n
}