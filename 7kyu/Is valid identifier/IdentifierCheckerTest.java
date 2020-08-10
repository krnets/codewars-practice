import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;


public class IdentifierCheckerTest {
    @Test
    public void testValid() {
        assertEquals(true, IdentifierChecker.isValid("i1"));
    }
    @Test
    public void testValid2() {
        assertEquals(true, IdentifierChecker.isValid("I1"));
    }

    @Test
    public void testInvalid() {
        assertEquals(false, IdentifierChecker.isValid("1i"));
    }
}