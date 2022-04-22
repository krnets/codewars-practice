import kotlin.test.assertEquals
import org.junit.Test

class TestExample {
    @Test
    fun basicTests() {
        assertEquals('f', addLetters(listOf('a', 'b', 'c')))
        assertEquals('z', addLetters(listOf('z')))
        assertEquals('c', addLetters(listOf('a', 'b')))
        assertEquals('c', addLetters(listOf('c')))
        assertEquals('a', addLetters(listOf('z', 'a')))
        assertEquals('d', addLetters(listOf('y', 'c', 'b')))
        assertEquals('z', addLetters(listOf()))
    }
}