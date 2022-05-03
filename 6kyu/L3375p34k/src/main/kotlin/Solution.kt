package com.codewars.hybris95

/*
class Leetspeak : Encoder() {
    private val toLeetMap = mapOf("a" to "4", "e" to "3", "l" to "1", "m" to "/^^\\", "o" to "0", "u" to "(_)")

    override fun encode(source: String?): String =
        source?.map { toLeetMap.getOrDefault("$it".lowercase(), "$it") }?.joinToString("") ?: ""
}

abstract class Encoder {
    abstract fun encode(source: String?): String
}
*/

class Leetspeak : Encoder() {
    override fun encode(source: String?): String = (source ?: "").map {
        when (it.lowercaseChar()) {
            'a' -> 4
            'e' -> 3
            'l' -> 1
            'm' -> "/^^\\"
            'o' -> 0
            'u' -> "(_)"
            else -> it
        }
    }.joinToString("")
}

abstract class Encoder {
    abstract fun encode(source: String?): String
}
