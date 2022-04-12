/*
class Kata {
    companion object {
        fun expressionsMatter(a: Int, b: Int, c: Int): Int {
            return listOf(
                a + b + c,
                (a + b) * c,
                a * (b + c),
                a * b * c,
            ).maxOrNull() ?: 0
        }
    }
}*/

import java.util.Collections.max

class Kata {
    companion object {
        fun expressionsMatter(a: Int, b: Int, c: Int): Int {
            return max(
                listOf(
                    a + b + c,
                    (a + b) * c,
                    a * (b + c),
                    a * b * c,
                )
            )
        }
    }
}
