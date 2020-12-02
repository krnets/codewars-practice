import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class TimeUtilsTest {

    @Test
    public void basicTest1() throws Exception {
        assertEquals("1 1 1 1", TimeUtils.convertTime(90061));
    }

    @Test
    public void basicTest2() throws Exception {
        assertEquals("-1 -1 -1 -1", TimeUtils.convertTime(-90061));
    }

    @Test
    public void shouldReturnZeroes() throws Exception {
        assertEquals("0 0 0 0", TimeUtils.convertTime(0));
        assertEquals("0 0 0 0", TimeUtils.convertTime(-0));
    }

    @Test
    public void shouldConvertSec() throws Exception {
        assertEquals("0 0 0 33", TimeUtils.convertTime(33));
        assertEquals("0 0 0 -33", TimeUtils.convertTime(-33));

        assertEquals("0 0 0 55", TimeUtils.convertTime(55));
        assertEquals("0 0 0 -55", TimeUtils.convertTime(-55));
    }

    @Test
    public void shouldConvertMin() throws Exception {
        assertEquals("0 0 1 38", TimeUtils.convertTime(98));
        assertEquals("0 0 -1 -38", TimeUtils.convertTime(-98));

        assertEquals("0 0 1 51", TimeUtils.convertTime(111));
        assertEquals("0 0 -1 -51", TimeUtils.convertTime(-111));
    }

    @Test
    public void shouldConvertHour() throws Exception {
        assertEquals("0 2 1 0", TimeUtils.convertTime(7260));
        assertEquals("0 -2 -1 0", TimeUtils.convertTime(-7260));
    }

    @Test
    public void shouldConvertDays() throws Exception {
        assertEquals("1 2 1 0", TimeUtils.convertTime(93660));
        assertEquals("-1 -2 -1 0", TimeUtils.convertTime(-93660));
    }
}