/*
fun reverse(a: List<String>): List<String> {
    val strMergedReversed = a.joinToString("").reversed()
    val list = mutableListOf<String>()
    var i = 0

    a.forEach {
        val sub = strMergedReversed.subSequence(i, i + it.length).toString()
        list.add(sub)
        i += it.length
    }
    return list
}*/

/*
fun reverse(a: List<String>): List<String> {
    val strMergedReversed = a.joinToString("").reversed()
    val list = mutableListOf<String>()
    var i = 0

    a.forEach {
        val sub = strMergedReversed.substring(i, it.length + i)
        list.add(sub)
        i += it.length
    }
    return list
}
*/

/*
fun reverse(a: List<String>): List<String> {
    val strIter = a.joinToString("").reversed().iterator()

    return a.map {
        Array(it.length) {
            strIter.nextChar()
        }.joinToString("")
    }
}
*/

/*
fun reverse(a: List<String>): List<String> {
    val str = a.joinToString("").reversed()
    var pos = 0

    return a.map {
        pos += it.length
        str.subSequence(pos - it.length, pos).toString()
    }
}
*/

fun reverse(a: List<String>): List<String> {
    val str = a.joinToString("").reversed()
    var pos = 0

    return a.map {
        pos += it.length
        str.drop(pos - it.length).take(it.length)
    }
}
