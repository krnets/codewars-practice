import kotlin.test.assertEquals
import org.junit.Test

class TestExample {
    @Test
    fun twenty() {
        val gen = paperFold()
        listOf(1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,0,1).iterator().forEach {
            assertEquals(it, gen.next())
        }
    }
}