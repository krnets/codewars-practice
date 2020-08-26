import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {
    @Test
    public void basicTests() {
        assertEquals(23, Solution.solve("123", 1));
        assertEquals(234, Solution.solve("1234", 1));
        assertEquals(34, Solution.solve("1234", 2));
        assertEquals(4, Solution.solve("1234", 3));
    }
}
