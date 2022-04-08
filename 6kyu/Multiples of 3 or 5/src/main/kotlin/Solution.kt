/*
fun solution(number: Int): Int {
    return (1 until number)
        .filter { it % 3 == 0 || it % 5 == 0 }
        .sum()
}*/

fun solution(number: Int): Int {
    return (3 until number step 3)
        .union(5 until number step 5)
        .sum()
}
