import kotlin.test.assertEquals
import org.junit.Test

class TestExample {
    @Test
    fun testFixed() {
        assertEquals("167773121", numberAndIPaddress("10.0.3.193"))
        assertEquals("10.3.3.193", numberAndIPaddress("167969729"))
    }
    @Test
    fun myTest() {
        assertEquals("2853672996", numberAndIPaddress("170.23.152.36"))
        assertEquals("169.164.33.131", numberAndIPaddress("2846105987"))
    }
}