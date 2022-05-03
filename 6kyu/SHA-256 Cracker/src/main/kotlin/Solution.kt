import java.math.BigInteger
import java.security.MessageDigest

fun crackSha256(hash: String, chars: String): String? = stringPermutationWithRecursion(chars)
    .firstOrNull {
        hash == "%064x".format(BigInteger(1, MessageDigest.getInstance("SHA-256").digest(it.toByteArray())))
    }

fun stringPermutationWithRecursion(string: String): Set<String> {
    if (string.length == 1)
        return setOf(string)

    val allCharsExceptLast = string.substringBeforeLast("")
    val lastChar = string.last()
    val permutations = stringPermutationWithRecursion(allCharsExceptLast)
    val allPermutations = mutableSetOf<String>()

    for (permutation in permutations) {
        val n = allCharsExceptLast.length
        for (i in 0..n) {
            val newP = permutation.substring(0, i) + lastChar + permutation.substring(i, n)
            allPermutations.add(newP)
        }
    }
    return allPermutations
}
