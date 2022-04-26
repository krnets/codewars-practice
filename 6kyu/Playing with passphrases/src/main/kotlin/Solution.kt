package solution

/*
object PlayPass {
    fun playPass(s: String, n: Int): String = s
        .mapIndexed { index, c ->
            if (index % 2 == 0)
                c.uppercase()
            else c.lowercase()
        }.joinToString("")
        .split(' ')
        .map { word ->
            word.map { c ->
                when {
                    c.isLowerCase() -> 'a' + (c - 'a' + n) % 26
                    c.isUpperCase() -> 'A' + (c - 'A' + n) % 26
                    c.isDigit() -> '0' + (9 - (c - '0'))
                    else -> c
                }
            }.joinToString("").reversed()
        }.reversed().joinToString(" ")
}*/

object PlayPass {
    fun playPass(s: String, n: Int): String = s.map { c ->
            when {
                c.isLetter() -> 'A' + (c - 'A' + n) % 26
                c.isDigit() -> '0' + ('9' - c)
                else -> c
            }
        }.mapIndexed { index, c ->
            if (index % 2 == 1 && c.isLetter())
                c.lowercase()
            else c
        }.reversed().joinToString("")
}
