/*
object DNADecomposer {
    fun decomposeDoubleStrand(doubleStrand: String): String {
        val frame1 = doubleStrand.chunked(3).joinToString(" ")
        val frame2 = (listOf(doubleStrand.take(1)) + doubleStrand.drop(1).chunked(3)).joinToString(" ")
        val frame3 = (listOf(doubleStrand.take(2)) + doubleStrand.drop(2).chunked(3)).joinToString(" ")

        val complementDNA = mapOf('A' to 'T', 'G' to 'C', 'T' to 'A', 'C' to 'G')
        val doubleStrandReversed = doubleStrand.reversed().map { complementDNA[it] }.joinToString("")

        val revFrame1 = doubleStrandReversed.chunked(3).joinToString(" ")
        val revFrame2 = (listOf(doubleStrandReversed.take(1)) + doubleStrandReversed.drop(1).chunked(3)).joinToString(" ")
        val revFrame3 = (listOf(doubleStrandReversed.take(2)) + doubleStrandReversed.drop(2).chunked(3)).joinToString(" ")

        return "Frame 1: $frame1\nFrame 2: $frame2\nFrame 3: $frame3\n\n" +
                "Reverse Frame 1: $revFrame1\nReverse Frame 2: $revFrame2\nReverse Frame 3: $revFrame3"
    }
}
*/

object DNADecomposer {
    fun decomposeDoubleStrand(doubleStrand: String): String {
        val complementDNA = mapOf('A' to 'T', 'G' to 'C', 'T' to 'A', 'C' to 'G')
        val dsRevComplement = doubleStrand.reversed().map { complementDNA[it] }.joinToString("")

        return "Frame 1: ${doubleStrand.chunked(3).joinToString(" ")}\n" +
                "Frame 2: ${doubleStrand.take(1)} ${doubleStrand.drop(1).chunked(3).joinToString(" ")}\n" +
                "Frame 3: ${doubleStrand.take(2)} ${doubleStrand.drop(2).chunked(3).joinToString(" ")}\n\n" +
                "Reverse Frame 1: ${dsRevComplement.chunked(3).joinToString(" ")}\n" +
                "Reverse Frame 2: ${dsRevComplement.take(1)} ${ dsRevComplement.drop(1).chunked(3).joinToString(" ") }\n" +
                "Reverse Frame 3: ${dsRevComplement.take(2)} ${dsRevComplement.drop(2).chunked(3).joinToString(" ")}"
    }
}

//            when (it) {
//                'A' -> 'T'
//                'G' -> 'C'
//                'T' -> 'A'
//                'C' -> 'G'
//                else -> it
//            }
