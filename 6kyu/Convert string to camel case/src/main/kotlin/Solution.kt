/*
fun toCamelCase(str: String): String = if (str.isEmpty()) str else str.first() +
        str.split("[_-]".toRegex())
            .joinToString("") { it.replaceFirstChar { c -> c.uppercaseChar() } }
            .drop(1)*/

/*
fun toCamelCase(str: String): String = if (str.isEmpty()) str else str.first() +
        str.split('-', '_')
            .joinToString("") { it.replaceFirstChar(Char::uppercase) }
            .drop(1)*/

//fun toCamelCase(str: String): String =
//    str.split("_|-".toRegex()).reduce { acc, s -> acc + s.replaceFirstChar(Char::uppercase) }

fun toCamelCase(str: String): String = str.split('_', '-')
    .reduce { acc, word -> acc + word.replaceFirstChar(Char::uppercase) }
