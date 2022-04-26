/*
fun bingo(ticket: Array<Pair<String, Int>>, win: Int): String {
    var countMiniWins = 0

    ticket.forEach { pair ->
        if (pair.first.any { it.code == pair.second })
            countMiniWins++
    }
    return if (countMiniWins >= win) "Winner!" else "Loser!"
}*/

/*
fun bingo(ticket: Array<Pair<String, Int>>, win: Int): String {
    return if (ticket.count { it.first.any { c -> c.code == it.second } } >= win) "Winner!" else "Loser!"
}
*/

fun bingo(ticket: Array<Pair<String, Int>>, win: Int): String {
    return if (ticket.count { it.second.toChar() in it.first } >= win) "Winner!" else "Loser!"
}
