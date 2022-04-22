package catmouse

/*
fun catMouse(s: String): String {
    return if (s.count { it == '.' } > 3) "Escaped!" else "Caught!"
}

*/

fun catMouse(s: String): String {
    return if (Math.abs(s.indexOf('C') - s.indexOf('m')) > 4) "Escaped!" else "Caught!"
}
