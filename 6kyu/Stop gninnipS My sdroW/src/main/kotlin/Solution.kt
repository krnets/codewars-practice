package spinwords

fun spinWords(sentence: String): String = sentence.split(" ")
    .joinToString(" ") { word ->
        if (word.length >= 5) word.reversed()
        else word
    }