import org.junit.jupiter.api.Test
import kotlin.test.*

class TestKata {
    @Test
    fun basicTests() {
        assertEquals(4, josephusSurvivor(7, 3))
        assertEquals(10, josephusSurvivor(11, 19))
        assertEquals(28, josephusSurvivor(40, 3))
        assertEquals(13, josephusSurvivor(14, 2))
        assertEquals(100, josephusSurvivor(100, 1))
        assertEquals(1, josephusSurvivor(1, 300))
        assertEquals(1, josephusSurvivor(2, 300))
        assertEquals(1, josephusSurvivor(5, 300))
        assertEquals(7, josephusSurvivor(7, 300))
        assertEquals(265, josephusSurvivor(300, 300))
    }
}