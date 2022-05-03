package simpson

/*
fun simpson(n: Int): Double {
    val h = Math.PI / n
    fun Fn(x: Double): Double = 1.5 * Math.pow(Math.sin(x), 3.0)

    return h / 3 * (1 until n / 2 + 1).sumOf {
        4 * Fn((2 * it - 1) * h) +
                2 * Fn((2 * it) * h)
    }
}*/

fun simpson(n: Int): Double = (Math.PI / n).let { h ->
    h / 3 * (1..(n / 2)).sumOf { i ->
        4 * Fn((2.0 * i - 1) * h) +
        2 * Fn((2.0 * i) * h)
    }
}

fun Fn(x: Double): Double = 1.5 * Math.pow(Math.sin(x), 3.0)
