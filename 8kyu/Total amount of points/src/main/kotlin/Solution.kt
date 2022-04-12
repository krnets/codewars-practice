/*
fun points(games: List<String>): Int {
    var sum = 0

    games.forEach { game ->
        val (x, y) = game.split(':')

        if (x > y) sum += 3
        else if (x == y) sum += 1
    }
    return sum
}
*/

/*
fun points(games: List<String>): Int {
    return games.map {
        val (x, y) = it.split(':')
        when {
            x > y -> 3
            x < y -> 0
            else -> 1
        }
    }.sum()
}
*/

fun points(games: List<String>): Int = games.fold(0) { sum, game ->
    val (x, y) = game.split(':')
    when {
        x > y -> sum + 3
        x < y -> sum + 0
        else -> sum + 1
    }
}
