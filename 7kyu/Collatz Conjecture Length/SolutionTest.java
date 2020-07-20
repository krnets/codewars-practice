import org.junit.Test;

import static org.junit.Assert.assertEquals;


public class SolutionTest {

    @Test
    public void testKnownValues() {
        assertEquals("Expected 8", 8, Collatz.conjecture(20));
    }
}
