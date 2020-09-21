import org.junit.Test;

import static org.junit.Assert.assertEquals;


public class SolutionTests {

    private static class DinglemouseAnswer20170727 {

        static String whatTimeIsIt(final double angle) {
            int min = (int) (60 * 12 * angle / 360);
            int hr = min / 60;
            min = min - hr * 60;
            if (hr == 0) hr = 12;
            return String.format("%02d:%02d", hr, min);
        }

    }

    @Test
    public void test1200() {
        assertEquals("12:00", Dinglemouse.whatTimeIsIt(0));
        assertEquals("12:00", Dinglemouse.whatTimeIsIt(360));
        assertEquals("12:28", Dinglemouse.whatTimeIsIt(14.0745d));
    }

    @Test
    public void test0300() {
        assertEquals("03:00", Dinglemouse.whatTimeIsIt(90));
    }

    @Test
    public void test0600() {
        assertEquals("06:00", Dinglemouse.whatTimeIsIt(180));
    }

    @Test
    public void test0900() {
        assertEquals("09:00", Dinglemouse.whatTimeIsIt(270));
    }

    @Test
    public void test30d() {
        assertEquals("01:00", Dinglemouse.whatTimeIsIt(30));
    }

    @Test
    public void test40d() {
        assertEquals("01:20", Dinglemouse.whatTimeIsIt(40));
    }

    @Test
    public void test45d() {
        assertEquals("01:30", Dinglemouse.whatTimeIsIt(45));
    }

    @Test
    public void test50d() {
        assertEquals("01:40", Dinglemouse.whatTimeIsIt(50));
    }

    @Test
    public void test60d() {
        assertEquals("02:00", Dinglemouse.whatTimeIsIt(60));
    }

    @Test
    public void testRandom() {
        for (int r = 0; r < 100; r++) {
            final double angle = Math.random() * 360;
            final String expected = DinglemouseAnswer20170727.whatTimeIsIt(angle);
            final String actual = Dinglemouse.whatTimeIsIt(angle);

            System.out.println(String.format("%gd = <span style='color:green'>%s</span>", angle, expected));
            assertEquals(expected, actual);
        }
    }

}