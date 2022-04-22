/*
fun predictAge(age1: Int, age2: Int, age3: Int, age4: Int, age5: Int, age6: Int, age7: Int, age8: Int): Int{
    return 0
}*/

fun predictAge(vararg ages: Int): Int {
    return (Math.sqrt(ages.sumOf { it * it }.toDouble()) / 2).toInt()
}
