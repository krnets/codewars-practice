/*
fun longToIP(ip: UInt): String = ip.toString(2)
    .padStart(32, '0')
    .chunked(8)
    .map { it.toInt(2) }
    .joinToString(".")*/

/*
fun longToIP(ip: UInt): String = ip.toString(2)
    .padStart(32, '0')
    .chunked(8)
    .joinToString(".") { it.toInt(2).toString() }
*/

/*
fun longToIP(ip: UInt): String = buildString {
    append((ip and 0xFF000000u) shr 24)
    append('.')
    append((ip and 0x00FF0000u) shr 16)
    append('.')
    append((ip and 0x0000FF00u) shr 8)
    append('.')
    append(ip and 0x000000FFu)
}
*/

/*
fun longToIP(ip: UInt): String = (0..24 step 8).map { ip shr it  and 255u }.reversed().joinToString(".")
*/

fun longToIP(ip: UInt): String = (24.downTo(0) step 8).map { octet -> ip shr octet and 255u }.joinToString(".")

/*
fun longToIP(ip: UInt): String = (24 downTo 0 step 8).joinToString(".") { "${ip.shr(it).toUByte()}" }
*/
