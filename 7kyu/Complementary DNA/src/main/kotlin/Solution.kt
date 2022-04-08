package dna

/*
fun makeComplement(dna: String): String {
    var dnaMap = mapOf('A' to 'T', 'T' to 'A', 'C' to 'G', 'G' to 'C')

    return dna.map { dnaMap.getOrDefault(it, ' ') }.joinToString("")
}*/

fun makeComplement(dna: String): String {
    var nucleoBase = "ACGT"
    var complementMap = nucleoBase.zip(nucleoBase.reversed()).toMap()

    return dna.map { complementMap.getOrDefault(it, ' ') }.joinToString("")
}
