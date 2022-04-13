package kata

object Kata {
    fun grid(n: Int): String? = if (n < 0) null else (0 until n)
        .joinToString("\n") {
            generateSequence(
                (it % 26 + 'a'.code).toChar()
            ) { c ->
                ((c.code - 'a'.code + 1) % 26 + 'a'.code).toChar()
            }.take(n).joinToString(" ")
        }
}

