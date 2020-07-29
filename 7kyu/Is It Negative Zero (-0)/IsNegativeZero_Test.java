import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class IsNegativeZero_Test {
    private NegativeZeroValidator solution = new NegativeZeroValidator();

    @Test
    public void basic_tests() throws Exception {
        assertEquals("", solution.isNegativeZero(-0f), true);
        assertEquals("", solution.isNegativeZero(-5f), false);
        assertEquals("", solution.isNegativeZero(-4f), false);
        assertEquals("", solution.isNegativeZero(-3f), false);
        assertEquals("", solution.isNegativeZero(-2f), false);
        assertEquals("", solution.isNegativeZero(-1f), false);
        assertEquals("", solution.isNegativeZero(0f), false);
        assertEquals("", solution.isNegativeZero(1f), false);
        assertEquals("", solution.isNegativeZero(2f), false);
        assertEquals("", solution.isNegativeZero(3f), false);
        assertEquals("", solution.isNegativeZero(4f), false);
        assertEquals("", solution.isNegativeZero(5f), false);
    }
} 