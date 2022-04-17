/*
fun moveTen(s: String): String {
    return s.map {
        ((it.code - 'a'.code + 10) % 26 + 'a'.code).toChar()
    }.joinToString("")
}*/

/*
fun moveTen(s: String): String {
    return s.map {
        'a' + (it - 'a' + 10) % 26
    }.joinToString("")
}*/

/*
fun moveTen(s: String): String {
    val abc = ('a'..'z')
    val shifted = ('a' + 10..'z')
    val lookup = abc.zip(shifted + abc)

    return s.map { lookup[it - 'a'].second }.joinToString("")
}
*/

fun moveTen(s: String): String {
    val abc = ('a'..'z')
    val lookup = abc.zip(abc.drop(10) + abc)

    return s.map { lookup[it - 'a'].second }.joinToString("")
}
