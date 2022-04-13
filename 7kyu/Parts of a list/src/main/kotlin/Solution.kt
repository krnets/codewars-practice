package partlist

/*
fun partlist(arr: Array<String>): Array<Array<String>> {
    val list = mutableListOf<Array<String>>()

    (1 until arr.size).forEach {
        var subList = mutableListOf<String>()

        subList.add(arr.take(it).joinToString(" "))
        subList.add(arr.drop(it).joinToString(" "))

        list.add(it - 1, subList.toTypedArray())
    }
    return list.toTypedArray()
}*/

fun partlist(arr: Array<String>): Array<Array<String>> {
    return (1 until arr.size).map {
        arrayOf(
            arr.take(it).joinToString(" "),
            arr.drop(it).joinToString(" ")
        )
    }.toTypedArray()
}