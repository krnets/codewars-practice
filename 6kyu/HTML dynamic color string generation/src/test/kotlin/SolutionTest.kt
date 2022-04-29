import org.junit.Test
import org.junit.Assert.assertEquals
import java.util.Random

class GenerateColorRGBTest {
    @Test
    @Throws(Exception::class)
    fun symbolTest() {
        assertEquals("#", GenerateColorRGB.generateColor(Random()).substring(0, 1))
    }
}