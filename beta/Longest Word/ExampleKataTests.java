import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class ExampleKataTests {
    @Test
    public void tests() {
        assertEquals("fgh", Kata.longestWord("a b c d e fgh"));
        assertEquals("three", Kata.longestWord("one two three"));
        assertEquals("grey", Kata.longestWord("red blue grey"));
    }
}