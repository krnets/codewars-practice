data class RGB(val r: Int, val g: Int, val b: Int)

/*
fun hexStringToRGB(hexString: String): RGB {
    val (r, g, b) = hexString.drop(1).chunked(2)

    return RGB(r.toInt(16), g.toInt(16), b.toInt(16))
}*/

/*
fun hexStringToRGB(hexString: String): RGB {
    val (r, g, b) = hexString.drop(1).chunked(2).map { it.toInt(16) }

    return RGB(r, g, b)
}
*/

fun hexStringToRGB(hexString: String): RGB {
    val (red, green, blue) = hexString.drop(1).chunked(2).map { it.toInt(16) }

    return RGB(red, green, blue)
}
