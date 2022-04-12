import org.junit.Test
import kotlin.test.assertEquals

class MissingLetterTests {

    @Test
    fun exampleTests() {
        assertEquals('e', findMissingLetter(charArrayOf('a', 'b', 'c', 'd', 'f')))
        assertEquals('P', findMissingLetter(charArrayOf('O', 'Q', 'R', 'S')))
    }
}