import org.junit.jupiter.api.Test
import kotlin.test.*

class ObservedPinTest {

    @Test
    fun `1 key press`() {
        assertContentEquals(
            listOf("5", "7", "8", "9", "0").sorted(),
            getPINs("8").sorted()
        )
    }

    @Test
    fun `2 key presses`() {
        assertContentEquals(
            listOf("11", "22", "44", "12", "21", "14", "41", "24", "42").sorted(),
            getPINs("11").sorted()
        )
    }

    @Test
    fun `3 key presses`() {
        assertContentEquals(
            listOf(
                "339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398",
                "256", "296", "259", "368", "638", "396", "238", "356", "659", "639", "666", "359",
                "336", "299", "338", "696", "269", "358", "656", "698", "699", "298", "236", "239"
            ).sorted(),
            getPINs("369").sorted()
        )
    }
}