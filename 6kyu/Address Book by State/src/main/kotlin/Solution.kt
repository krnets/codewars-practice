package solution

/*
object State {
    fun byState(str: String): String {
        val data = str.split("\n")
            .sortedWith(compareBy({ it.takeLast(2) }, { it.takeWhile { c -> c != ' ' } }))

        val states = mapOf( "AZ" to "Arizona", "CA" to "California", "ID" to "Idaho", "IN" to "Indiana", "MA" to "Massachusetts", "OK" to "Oklahoma", "PA" to "Pennsylvania", "VA" to "Virginia" )
        val sortedMap = mutableMapOf<String, MutableList<String>>()

        data.forEach {
            val s = states.getOrDefault(it.takeLast(2), "")
            val t = ".".repeat(5) + " " + it.dropLast(2).replace(",", "")

            if (sortedMap.containsKey(s))
                sortedMap[s]!!.add(t)
            else sortedMap[s] = mutableListOf(t)
        }
        return sortedMap.map { (state, address) ->
            " $state\n" + address.joinToString("\n") { it + state }
        }.joinToString("\n").trimStart()
    }
}*/

/*
object State {
    fun byState(str: String): String {
        val states = mapOf( "AZ" to "Arizona", "CA" to "California", "ID" to "Idaho", "IN" to "Indiana", "MA" to "Massachusetts", "OK" to "Oklahoma", "PA" to "Pennsylvania", "VA" to "Virginia" )

        return str.split("\n")
            .sortedWith(compareBy { it.takeLast(2) })
            .groupBy({ states[it.takeLast(2)] }, { it })
            .map { (state, addresses) ->
                "$state" + addresses.sorted().joinToString("\n..... ", "\n..... ") {
                    "${it.split(',').joinToString("").dropLast(2)}$state"
                }
            }.joinToString("\n ")
    }
}
*/

object State {
    fun byState(str: String): String {
        val states = mapOf( "AZ" to "Arizona", "CA" to "California", "ID" to "Idaho", "IN" to "Indiana", "MA" to "Massachusetts", "OK" to "Oklahoma", "PA" to "Pennsylvania", "VA" to "Virginia" )

        return str.split("\n")
            .sortedWith(compareBy { it.takeLast(2) })
            .groupBy({ states[it.takeLast(2)] }, { it.dropLast(2) })
            .map { (state, addresses) ->
                "$state" + addresses.sorted().joinToString("\n..... ", "\n..... ") {
                    "${it.split(',').joinToString("")}$state"
                }
            }.joinToString("\n ")
    }
}
