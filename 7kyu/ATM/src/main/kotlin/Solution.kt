package solution

/*
fun count(number: Int): Int {
    val bankNotes = listOf(10, 20, 50, 100, 200, 500)
    var currentAmount = number
    var count = 0

    bankNotes.reversed().forEach {
        if (currentAmount >= it) {
            count += currentAmount / it
            currentAmount %= it
        }
    }
    return if (currentAmount == 0) count else -1
}*/

fun count(number: Int): Int {
    val bankNotes = listOf(10, 20, 50, 100, 200, 500)

    val (rem, count) = bankNotes.foldRight(Pair(number, 0)) { bankNote, (rem, count) ->
        Pair(rem % bankNote, count + rem / bankNote)
    }
    return if (rem == 0) count else -1
}
