/*
fun josephusSurvivor(n: Int, k: Int): Int {
    val people = (1..n).toMutableList()
    var remaining = n
    var counter = k

    while (true) {

        for (i in 0 until n) {

            if (people[i] > 0) {

                if (remaining == 1)
                    return people[i]

                counter--

                if (counter == 0) {

                    people[i] = -people[i]
                    remaining--
                    counter = k
                }
            }
        }
    }
}*/

/*
fun josephusSurvivor(n: Int, k: Int): Int {
    var people = (1..n).toMutableList()
    var remaining = n
    var counter = k

    while (true) {
        val survivors = mutableListOf<Int>()

        for (i in people.indices) {
            if (remaining == 1)
                return people[i]

            counter--

            if (counter > 0)
                survivors.add(people[i])
            else {
                remaining--
                counter = k
            }
        }
        people = survivors
    }
}
*/

/*
fun josephusSurvivor(n: Int, k: Int): Int {
    val list = (1..n).toMutableList()
    var pos = 0

    while (list.size > 1) {
        pos = (pos + k - 1) % list.size
        list.removeAt(pos)
    }

    return list.first()
}
*/

fun josephusSurvivor(n: Int, k: Int): Int {
    var survivor = 0

    for (i in 2..n) {
        survivor = (survivor + k) % i
    }
    return survivor + 1
}

/*
fun josephusSurvivor(n: Int, k: Int): Int {
    return (1..n).fold(1) { i, j -> (i + k) % j } + 1
}
*/
