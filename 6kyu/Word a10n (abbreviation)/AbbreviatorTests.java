import static org.junit.Assert.*;

import org.junit.Test;

public class AbbreviatorTests {

    private Abbreviator abbr = new Abbreviator();

    @Test
    public void testInternationalization() {
        assertEquals("i18n", abbr.abbreviate("internationalization"));
    }

    @Test
    public void testExample() {
        assertEquals("e6t-r3s are r4y fun!", abbr.abbreviate("elephant-rides are really fun!"));
    }

    @Test
    public void testThrowTheKitchenSinkAtEm() {
        assertEquals("s2s5b5n b5n sat_d4e-b6d5d4e-b6d cat-the; sat", abbr
                .abbreviate("sits5balloon balloon sat_double-barreled5double-barreled cat-the; sat"));
    }

}