import kotlin.test.assertEquals
import org.junit.Test

class TestExample {
    @Test
    fun `Basic Tests`() {
        assertEquals("*********\n* olleH *\n* dlroW *\n*********", mirror("Hello World"))
        assertEquals(
            "************\n" +
                    "* srawedoC *\n" +
                    "************", mirror("Codewars")
        )
    }

    @Test
    fun `Extra Tests`() {
        assertEquals(
            "**********\n" +
                    "* gwxe   *\n" +
                    "* amjc   *\n" +
                    "* ykdkuk *\n" +
                    "**********",
            mirror("exwg cjma kukdky")
        )
    }
}
