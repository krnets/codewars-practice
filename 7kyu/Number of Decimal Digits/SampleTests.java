import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class SampleTests {
    @Test
    public void Digits() {
        assertEquals(1,  DecTools.Digits(5l));
        assertEquals(5,  DecTools.Digits(12345l));
        assertEquals(10, DecTools.Digits(9876543210l));
    }
}