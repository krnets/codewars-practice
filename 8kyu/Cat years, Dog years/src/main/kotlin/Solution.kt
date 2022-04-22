package solution

fun calculateYears(years: Int): Array<Int> {
    var catYears = 0
    var dogYears = 0

    if (years > 0) {
        catYears += 15
        dogYears += 15
    }
    if (years > 1) {
        catYears += 9
        dogYears += 9
    }
    if (years > 2) {
        catYears += 4 * (years - 2)
        dogYears += 5 * (years - 2)
    }
    return arrayOf(years, catYears, dogYears);
}