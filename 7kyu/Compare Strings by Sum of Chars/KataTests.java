import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class KataTests {
    @Test
    public void BasicTests() {
        assertEquals(true, Kata.compare("AD", "BC"));
        assertEquals(false, Kata.compare("AD", "DD"));
    }
}