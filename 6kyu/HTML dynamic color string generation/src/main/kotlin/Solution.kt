import java.util.Random

/*
object GenerateColorRGB {
    fun generateColor(r: Random): String {
        val RR = r.nextInt(256)
        val GG = r.nextInt(256)
        val BB = r.nextInt(256)

        return "#" + "%02x".repeat(3).format(RR, GG, BB)
    }
}*/

/*
object GenerateColorRGB {
    fun generateColor(r: Random): String = "#" + (1..3).joinToString("") { "%02x".format(r.nextInt(256)) }
}
*/

/*
object GenerateColorRGB {
    fun generateColor(r: Random): String = (1..3).joinToString("", "#") { "%02x".format(r.nextInt(256)) }
}
*/

object GenerateColorRGB {
    fun generateColor(r: Random): String = "#%06x".format(r.nextInt(0xFF_FF_FF + 1))
}
