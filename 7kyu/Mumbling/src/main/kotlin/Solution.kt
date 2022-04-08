package accum

/*
fun accum(s: String): String {
    var sb = StringBuilder()

    s.forEachIndexed { index, c ->

        sb.append(c.uppercaseChar())
        sb.append(c.lowercaseChar().toString().repeat(index))
        sb.append('-')
    }
    return sb.toString().dropLast(1)
}*/

fun accum(s: String): String =
    s.mapIndexed { index, c -> c.uppercaseChar() + c.lowercase().repeat(index) }.joinToString("-")