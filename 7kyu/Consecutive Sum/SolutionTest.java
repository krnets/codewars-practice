import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {
    @Test
    public void exampleTests() {
        assertEquals(1, Kata.consecutiveSum(1));
        assertEquals(4, Kata.consecutiveSum(15));
        assertEquals(2, Kata.consecutiveSum(48));
        assertEquals(2, Kata.consecutiveSum(97));
    }
}
