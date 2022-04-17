/*
object FixStringCase {
    fun solve(s: String): String {
        val countUpper = s.count { it.isUpperCase() }
        return if (countUpper > s.length / 2) s.uppercase() else s.lowercase()
    }
}*/

object FixStringCase {
    fun solve(s: String): String =
        if (s.count { it.isUpperCase() } > s.length / 2) s.uppercase()
        else s.lowercase()
}
