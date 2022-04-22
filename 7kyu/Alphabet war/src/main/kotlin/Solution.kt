/*
fun alphabetWar(fight: String): String {
    val left = "sbpw"
    val right = "zdqm"
    val (leftHits, rightHits) = fight.partition { left.contains(it) }
    val leftSum = leftHits.sumOf { left.indexOf(it) + 1 }
    val rightSum = rightHits.sumOf { right.indexOf(it) + 1 }

    return when {
        leftSum > rightSum -> "Left side wins!"
        rightSum > leftSum -> "Right side wins!"
        else -> "Let's fight again!"
    }
}*/

fun alphabetWar(fight: String): String {
    val left = "sbpw"
    val right = "zdqm"
    val power = fight.sumOf { (left.indexOf(it) + 1) - (right.indexOf(it) + 1) }

    return when {
        power > 0 -> "Left side wins!"
        power < 0 -> "Right side wins!"
        else -> "Let's fight again!"
    }
}

/*
fun alphabetWar(fight: String): String {
    val points = fight.fold(0) { score, letter ->
        score + when (letter) {
            'w' -> -4
            'p' -> -3
            'b' -> -2
            's' -> -1
            'm' -> 4
            'q' -> 3
            'd' -> 2
            'z' -> 1
            else -> 0
        }
    }
    return when {
        points < 0 -> "Left side wins!"
        points > 0 -> "Right side wins!"
        else -> "Let's fight again!"
    }
}
*/

/*
fun alphabetWar(fight: String): String {
    return fight.fold(0) { score, letter ->
        score + when (letter) {
            'w' -> -4
            'p' -> -3
            'b' -> -2
            's' -> -1
            'm' -> 4
            'q' -> 3
            'd' -> 2
            'z' -> 1
            else -> 0
        }
    }.let {
        when {
            it < 0 -> "Left side wins!"
            it > 0 -> "Right side wins!"
            else -> "Let's fight again!"
        }
    }
}*/
