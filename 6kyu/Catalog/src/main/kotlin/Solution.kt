/*
fun catalog(s: String, article: String): String = s.split("\n")
    .filter { it.contains(article) }
    .joinToString("\n") {
        val name = it.substring(it.indexOf("<name>") + "<name>".length, it.indexOf("</name>"))
        val price = it.substring(it.indexOf("<prx>") + "<prx>".length, it.indexOf("</prx>"))
        val qty = it.substring(it.indexOf("<qty>") + "<qty>".length, it.indexOf("</qty>"))
        "$name > prx: $$price qty: $qty"
    }.let { it.ifEmpty { "Nothing" } }*/

/*
fun catalog(s: String, article: String): String = s.split("\n")
    .filter { it.contains(article) }
    .joinToString("\n") {
        val name = it.substringAfter("<name>").substringBefore("</name>")
        val price = it.substringAfter("<prx>").substringBefore("</prx>")
        val qty = it.substringAfter("<qty>").substringBefore("</qty>")
        "$name > prx: $$price qty: $qty"
    }.let { it.ifEmpty { "Nothing" } }
*/

/*
fun catalog(s: String, article: String): String = s.split("\n")
    .filter { it.contains(article) }
    .joinToString("\n") {
        val name = it.substringAfter("<name>").substringBefore("</name>")
        val price = it.substringAfter("<prx>").substringBefore("</prx>")
        val qty = it.substringAfter("<qty>").substringBefore("</qty>")
        "$name > prx: $$price qty: $qty"
    }.ifEmpty { "Nothing" }
*/

fun catalog(s: String, article: String): String =
    Regex("""<prod><name>(.+)</name><prx>(.+)</prx><qty>(.+)</qty></prod>""")
        .findAll(s)
        .filter { it.groupValues[1].contains(article) }
        .joinToString("\n") {
            val (_, name, price, qty) = it.groupValues
            "$name > prx: $$price qty: $qty"
        }.ifEmpty { "Nothing" }

/*
fun catalog(s: String, article: String): String =
    Regex("""^<prod><name>(.+)</name><prx>(.+)</prx><qty>(.+)</qty></prod>$""", RegexOption.MULTILINE)
        .findAll(s)
        .filter { it.groupValues[1].contains(article) }
        .joinToString("\n") {
            val (_, name, price, qty) = it.groupValues
            "$name > prx: $$price qty: $qty"
        }.ifEmpty { "Nothing" }
*/
