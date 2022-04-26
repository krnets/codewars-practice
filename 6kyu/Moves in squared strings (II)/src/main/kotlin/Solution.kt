package solution

/*
object Opstrings {

    fun rot(strng: String): String = strng.reversed()

    fun selfieAndRot(strng: String): String {
        val s = strng.split('\n').map { it + ".".repeat(it.length) }
        val t = s.joinToString("\n")
        val u = s.reversed().joinToString("\n") { it.reversed() }

        return "$t\n$u"
    }

    fun oper(f: (String) -> String, s: String): String = f(s)
}*/

/*
object Opstrings {

    fun rot(strng: String): String = strng.reversed()

    fun selfieAndRot(strng: String): String {
        val s = strng.split('\n').map { it + ".".repeat(it.length) }
        val t = s.joinToString("\n")
        val u = s.reversed().joinToString("\n") { rot(it) }

        return "$t\n$u"
    }

    fun oper(f: (String) -> String, s: String): String = f(s)
}
*/

object Opstrings {
    fun rot(strng: String): String = strng.reversed()

    fun selfieAndRot(strng: String): String = strng.split('\n')
        .joinToString("\n") { it + ".".repeat(it.length) }
        .let { it + '\n' + rot(it) }

    fun oper(f: (String) -> String, s: String): String = f(s)
}
