package solution

object Suite2 {
    fun game(n: Long): String =
        if (n % 2 == 1L)
            "[${n * n}, 2]"
        else "[${n * n / 2}]"
}