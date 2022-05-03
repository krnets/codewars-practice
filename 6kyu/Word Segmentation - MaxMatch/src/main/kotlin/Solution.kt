fun maxMatch(sentence: String): List<String> {
    val words = mutableListOf<String>()
    var i = sentence.length

    while (i > 0) {
        val word = sentence.substring(0, i)

        if (i == 1 || VALID_WORDS.contains(word)) {
            words.add(word)
            words.addAll(maxMatch(sentence.substring(i)))
            break
        }
        i--
    }
    return words
}

val VALID_WORDS = setOf("good", "luck", "in")
