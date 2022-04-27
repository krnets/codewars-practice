package pianoKataPartTwo

/*
fun whichNote(keyPressCount: Int): String {
    val pianoKeys = arrayOf("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#")

    return pianoKeys[(keyPressCount - 1) % 88 % 12]
}
*/

/*
fun whichNote(keyPressCount: Int): String =
    arrayOf("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#")[(keyPressCount - 1) % 88 % 12]*/

fun whichNote(keyPressCount: Int): String = "A A# B C C# D D# E F F# G G#".split(' ')[(keyPressCount - 1) % 88 % 12]
