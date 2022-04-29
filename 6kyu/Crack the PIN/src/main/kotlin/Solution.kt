package algos

import java.math.BigInteger
import java.security.MessageDigest

/*
fun crack(hash: String): String {
    var result = ""

    for (i in 0..99999) {
        val pinStr = "$i".padStart(5, '0')
        val byteArr = pinStr.toByteArray()
        val h = MessageDigest.getInstance("MD5").digest(byteArr)
            .joinToString("") {
                String.format("%02x", it)
            }
        if (h == hash) {
            result = pinStr
            break
        }
    }

    return result
}*/

/*
fun crack(hash: String): String = (0..99999)
    .map { "$it".padStart(5, '0') }
    .firstOrNull {
        MessageDigest.getInstance("MD5").digest(it.toByteArray())
            .joinToString("") { byte ->
                String.format("%02x", byte)
            } == hash
    } ?: ""
*/

/*
fun crack(hash: String): String = (0..99999)
    .map { "$it".padStart(5, '0') }
    .firstOrNull {
        BigInteger(
            1,
            MessageDigest.getInstance("MD5").digest(it.toByteArray())
        ).toString(16) == hash
    } ?: ""
*/

fun crack(hash: String): String = (0..99999)
    .map { "$it".padStart(5, '0') }
    .firstOrNull {
        BigInteger(
            1,
            MessageDigest.getInstance("MD5").digest(it.toByteArray())
        ).toString(16).padStart(32, '0') == hash
    } ?: ""

/*
4x slower than above

fun crack(hash: String): String = (0..99999)
    .map { "$it".padStart(5, '0') }
    .firstOrNull {
        MessageDigest.getInstance("MD5").digest(it.toByteArray()).joinToString("") { "%02x".format(it) } == hash
    } ?: ""
*/

/*
fun crack(hash: String): String = (0..99999)
    .map { "$it".padStart(5, '0') }
    .firstOrNull {
        hash == "%032x".format(BigInteger(1, MessageDigest.getInstance("MD5").digest(it.toByteArray())))
    } ?: ""
*/

/*
fun crack(hash: String): String = (0..99999)
    .map { "%05d".format(it) }
    .firstOrNull {
        hash == "%032x".format(BigInteger(1, MessageDigest.getInstance("MD5").digest(it.toByteArray())))
    } ?: ""
*/
