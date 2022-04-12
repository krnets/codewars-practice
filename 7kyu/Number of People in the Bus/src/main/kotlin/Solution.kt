/*
fun people(busStops: Array<Pair<Int, Int>>): Int {
    var onTheBus = 0

    busStops.forEach {
        onTheBus += it.first
        onTheBus -= it.second
    }
    return onTheBus
}*/

/*
fun people(busStops: Array<Pair<Int, Int>>): Int =
    busStops.fold(0) { peopleOnTheBus, busStop -> peopleOnTheBus + busStop.first - busStop.second }
*/

fun people(busStops: Array<Pair<Int, Int>>): Int = busStops.sumOf { it.first - it.second }
