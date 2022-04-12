/*
fun inArray(array1: Array<String>, array2: Array<String>): Array<String> =
    array1.filter { s -> array2.any { it.contains(s) } }
        .toSortedSet()
        .toTypedArray()
*/

fun inArray(array1: Array<String>, array2: Array<String>): Array<String> =
    array1.distinct()
        .filter { s -> array2.any { it.contains(s) } }
        .sorted()
        .toTypedArray()
