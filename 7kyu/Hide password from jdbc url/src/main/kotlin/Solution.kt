/*
object PasswordHider {
    fun hidePasswordFromConnection(urlString: String): String {
        val pattern = "(?<=password=[^&]{0,20})[^&]".toRegex()
        return urlString.replace(pattern, "*")
    }
}
*/

/*
object PasswordHider {
    fun hidePasswordFromConnection(urlString: String): String {
        return Regex("(?<=password=)[^&]*").replace(urlString) { "*".repeat(it.value.length) }
    }
}
*/

object PasswordHider {
    fun hidePasswordFromConnection(urlString: String): String {
        return with(urlString.substringAfter("password=").substringBefore("&")) {
            urlString.replace(this, this.map { '*' }.joinToString(""))
        }
    }
}

