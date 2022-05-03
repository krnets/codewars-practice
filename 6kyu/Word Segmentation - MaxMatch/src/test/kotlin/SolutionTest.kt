import kotlin.test.assertEquals
import org.junit.Test

class ExampleTest {
    @Test
    fun goodLuck() {
        assertEquals(listOf("good", "luck"), maxMatch("goodluck"))
    }
    @Test
    fun invalidWord() {
        // "invalid" just means the word, "ewingsa", is not in the Set VALID_WORDS
        assertEquals(listOf("e","w","in","g","s","a"), maxMatch("ewingsa"))
    }
}