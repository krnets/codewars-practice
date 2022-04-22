/*
fun growingPlant(upSpeed: Int, downSpeed: Int, desiredHeight: Int): Int {
    var height = 0
    var count = 0

    while (height < desiredHeight) {
        height += upSpeed
        count++
        if (height >= desiredHeight)
            break
        height -= downSpeed
    }
    return count
}*/

/*
fun growingPlant(upSpeed: Int, downSpeed: Int, desiredHeight: Int): Int {
    return generateSequence(
        upSpeed to (upSpeed - downSpeed)
    ) {
        it.second + upSpeed to it.second + upSpeed - downSpeed
    }.takeWhile { it.first < desiredHeight }
        .count() + 1
}
*/

/*
fun growingPlant(upSpeed: Int, downSpeed: Int, desiredHeight: Int): Int {
    return Math.max(
        1.0,
        Math.ceil((desiredHeight - downSpeed).toDouble() / (upSpeed - downSpeed))
    ).toInt()
}
*/

tailrec fun growingPlant(upSpeed: Int, downSpeed: Int, desiredHeight: Int): Int {
    return if (upSpeed >= desiredHeight) 1
    else 1 + growingPlant(upSpeed, downSpeed, desiredHeight - upSpeed + downSpeed)
}
