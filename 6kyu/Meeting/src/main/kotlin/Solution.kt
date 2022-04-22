/*
fun meeting(s: String): String = s.split(";")
    .map {
        val (firstName, lastName) = it.split(":")
        "(${lastName.uppercase()}, ${firstName.uppercase()})"
    }
    .sorted()
    .joinToString("")
*/

/*
fun meeting(s: String): String = s.uppercase().split(";")
    .map {
        val (firstName, lastName) = it.split(":")
        "(${lastName}, ${firstName})"
    }
    .sorted()
    .joinToString("")
*/
fun meeting(s: String): String = s.uppercase().split(";")
    .map { it.split(":") }
//    .sortedWith(compareBy({ it[1] }, { it[0] }))
    .sortedWith(compareBy({ it.last() }, { it.first() }))
    .joinToString("") { "(${it.last()}, ${it.first()})" }

/*
fun meeting(s: String): String = s.split(";")
    .map {
        it.uppercase().replace(Regex("(\\w+):(\\w+)"), "($2, $1)")
    }
    .sorted()
    .joinToString("")
*/
