/*
fun persistence(num: Int): Int =
    if (num < 10) 0
    else 1 + persistence(num.toString().map { it.code - '0'.code } .fold(1) { x, y -> x * y } )*/

fun persistence(num: Int): Int =
    if (num < 10) 0
    else 1 + persistence(num.toString().map(Character::getNumericValue).reduce(Int::times))