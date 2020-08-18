import static org.junit.Assert.*;

import org.junit.Test;

public class BraceCheckerTests {

    private BraceChecker checker = new BraceChecker();

    @Test
    public void testValid() {
        assertEquals(true, checker.isValid("()"));
    }

    @Test
    public void testValidAll() {
        assertEquals(true, checker.isValid("([{}])"));
    }

    @Test
    public void testValidWithSpaces() {
        assertEquals(true, checker.isValid("(  )"));
    }

    @Test
    public void testValidWithSpacesOutside() {
        assertEquals(true, checker.isValid(" () "));
    }

    @Test
    public void testInvalidSimple() {
        assertEquals(false, checker.isValid("(}"));
    }

    @Test
    public void testInvalid() {
        assertEquals(false, checker.isValid("[(])"));
    }

    @Test
    public void testInvalidAll() {
        assertEquals(false, checker.isValid("[({})](]"));
    }
}