import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class PrimitiveTest {

    Primitive p = new Primitive();

    @Test
    public void testByte() {
        assertEquals("byte", p.determineType("2"));
    }

    @Test
    public void testInt() {
        assertEquals("int", p.determineType("-803847"));
    }

    @Test
    public void testNone() {
        assertEquals("none", p.determineType("9173654782928177561848183754729818437466"));
    }

    @Test
    public void testShort() {
        assertEquals("short", p.determineType("3573"));
    }

    @Test
    public void testLong() {
        assertEquals("long", p.determineType("-5745621829365"));
    }
}