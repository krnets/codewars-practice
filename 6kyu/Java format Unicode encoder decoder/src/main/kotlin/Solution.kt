/*
object JavaUnicodeEncoder {
    fun decode(input: String?): String = input!!.split("\\u")
        .filterNot { it.isEmpty() }
        .map {
            Integer.parseInt(it, 16).toChar()
        }.joinToString("")

    fun encode(input: String?): String = input!!.map {
        String.format("\\u%04x", it.code)
    }.joinToString("")
}*/

object JavaUnicodeEncoder {
    fun decode(input: String?): String = input!!.split("\\u").drop(1)
        .map {
            it.toInt(16).toChar()
        }.joinToString("")

    fun encode(input: String?): String = input!!.map {
        "\\u%04x".format(it.code)
    }.joinToString("")
}
