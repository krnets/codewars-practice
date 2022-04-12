/*
fun findMissingLetter(array: CharArray): Char {
    return array.zip(array.drop(1))
        .first { it.second - it.first > 1 }
        .first + 1
}*/

/*
fun findMissingLetter(array: CharArray): Char {
    return (array.first()..array.last())
        .first { it !in array }
}
*/

/*
fun findMissingLetter(array: CharArray): Char {
    return (array.first()..array.last())
        .first { !array.contains(it) }
}
*/

fun findMissingLetter(array: CharArray): Char {
    return (array.first()..array.last())
        .filterNot { it in array }.first()
}
