/*
fun addLetters(arr: List<Char>): Char {
    return if (arr.isEmpty()) 'z'
    else 'a' + (arr.sumOf { it - 'a' + 1 } - 1) % 26
}*/

fun addLetters(arr: List<Char>): Char {
    return 'z' - arr.sumOf { 'z' - it }.mod(26)
}
