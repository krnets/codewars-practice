fun f(n: Int): Int = if (n == 0) 1 else n - m(f(n - 1))

fun m(n: Int): Int = if (n == 0) 0 else n - f(m(n - 1))