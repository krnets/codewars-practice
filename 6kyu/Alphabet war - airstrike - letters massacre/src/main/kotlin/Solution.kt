/*
fun alphabetWar(fight: String): String {
    var leftSideScore = 0
    var rightSideScore = 0
    val leftSideLetters = " sbpw"
    val rightSideLetters = " zdqm"
    val postAirstrike = fight.toCharArray()

    for (i in fight.indices) {
        if (fight[i] == '*') {
            postAirstrike[i] = '_'
            if (i > 0) postAirstrike[i - 1] = '_'
            if (i < fight.lastIndex) postAirstrike[i + 1] = '_'
        }
    }
    postAirstrike.forEach {
        if (leftSideLetters.contains(it))
            leftSideScore += leftSideLetters.indexOf(it)
        else if (rightSideLetters.contains(it))
            rightSideScore += rightSideLetters.indexOf(it)
    }
    return when {
        leftSideScore > rightSideScore -> "Left side wins!"
        leftSideScore < rightSideScore -> "Right side wins!"
        else -> "Let's fight again!"
    }
}*/

fun alphabetWar(fight: String): String {
    val left = " sbpw"
    val right = " zdqm"

    return fight.replace(Regex("\\w?\\*\\w?"), "")
        .sumOf {
            when (it) {
                in left -> -left.indexOf(it)
                in right -> right.indexOf(it)
                else -> 0
            }
        }
        .let {
            when {
                it < 0 -> "Left side wins!"
                it > 0 -> "Right side wins!"
                else -> "Let's fight again!"
            }
        }
}
