/*
import kotlin.math.*

fun rgb(r: Int, g: Int, b: Int): String {
    var rr = max(min(r, 255), 0)
    var gg = max(min(g, 255), 0)
    var bb = max(min(b, 255), 0)

    return String.format("%02X%02X%02X", rr, gg, bb)
}*/

/*
fun rgb(r: Int, g: Int, b: Int): String =
    String.format("%02X%02X%02X", r.coerceIn(0..255), g.coerceIn(0..255), b.coerceIn(0..255))
*/

/*
fun rgb(r: Int, g: Int, b: Int): String = listOf(r, g, b)
    .joinToString("") { "%02X".format(it.coerceIn(0..255)) }
*/

fun rgb(vararg colours: Int): String =
    colours.joinToString("") {
        "%02X".format(it.coerceIn(0..255))
    }

