package kata

/*
object KataSolution {
    fun longestRepetition(s: String): Pair<Char?, Int> {
        if (s.isEmpty()) return null to 0

        val pattern = "(.)(\\1+)".toRegex()
        val matches = pattern.findAll(s).map { it.value }.toList()

        if (matches.isEmpty()) return s.first() to 1

        val longest = matches.maxOfOrNull { it.length } ?: 0
        val ans = matches.first { it.length == longest }

        return ans.first() to ans.length
    }
}*/

object KataSolution {
    fun longestRepetition(s: String): Pair<Char?, Int> = "(.)\\1*".toRegex()
        .findAll(s)
        .map { it.value }
        .maxByOrNull { it.length }
        ?.let {
            it.first() to it.length
        } ?: Pair(null, 0)
}
