package travel

fun travel(r: String, zipcode: String): String {
    if (!Regex("""[A-Z]{2} \d{5}""").matches(zipcode))
        return "$zipcode:/"

    val clientAddresses = r.split(',')
        .filter { it.endsWith(zipcode) }
        .map { Regex("""(\d+) (.*) ([A-Z]{2} \d{5})""").findAll(it) }

    return "$zipcode:" +
            clientAddresses.joinToString(",") { it.first().groups[2]!!.value } + '/' +
            clientAddresses.joinToString(",") { it.first().groups[1]!!.value }
}