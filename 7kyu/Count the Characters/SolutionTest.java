import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class SolutionTest {
    @Test
    public void testSomething() {
        assertEquals(4, CC.charCount("fizzbuzz", 'z'));
        assertEquals(4, CC.charCount("FIZZBUZZ", 'z'));
    }
}