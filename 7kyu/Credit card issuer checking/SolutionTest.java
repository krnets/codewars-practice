import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class SolutionTest {
    @Test
    public void issuerTests() {
        assertEquals("AMEX",       Kata.getIssuer("378282246310005"));
        assertEquals("Discover",   Kata.getIssuer("6011111111111117"));
        assertEquals("Mastercard", Kata.getIssuer("5105105105105100"));
        assertEquals("VISA",       Kata.getIssuer("4111111111111111"));
        assertEquals("Unknown",    Kata.getIssuer("9111111111111111"));
    }
}