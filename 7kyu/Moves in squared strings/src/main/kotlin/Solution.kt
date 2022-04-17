package solution

object Opstrings {

    fun vertMirror(strng: String): String = strng.split('\n')
        .joinToString("\n") { it.reversed() }

    fun horMirror(strng: String): String = strng.split('\n').reversed()
        .joinToString("\n")

    fun oper(f: (String) -> String, s: String): String = f(s)
}