/*
fun solution(input: String, markers: CharArray): String {
    return input.split("\n").map {
        it.takeWhile { c -> c !in markers }.trimEnd()
    }.joinToString("\n")
}
*/

/*
fun solution(input: String, markers: CharArray): String =
    input.lines().joinToString("\n") { it.split(*markers).first().trimEnd() }
*/

fun solution(input: String, markers: CharArray): String =
    input.lines().joinToString("\n") { line ->
        line.takeWhile { c -> c !in markers }
            .trimEnd()
    }
