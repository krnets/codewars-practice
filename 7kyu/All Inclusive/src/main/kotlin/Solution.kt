package allinclusive

/*
fun containAllRots(strng: String, arr: ArrayList<String>): Boolean = strng.indices
    .map { strng.substring(it) + strng.substring(0, it) }
    .all { arr.contains(it) }*/

fun containAllRots(strng: String, arr: ArrayList<String>): Boolean =
    arr.containsAll(strng.indices.map { strng.drop(it) + strng.take(it) })

/*
fun containAllRots(strng: String, arr: ArrayList<String>): Boolean =
    arr.containsAll(strng.indices.map { strng.takeLast(it) + strng.dropLast(it) })
*/

/*
fun containAllRots(strng: String, arr: ArrayList<String>): Boolean =
    arr.containsAll(List(strng.length) { strng.drop(it) + strng.take(it) })
*/
