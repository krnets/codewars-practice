import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class HumanReadableTimeTest {
    @Test
    public void Tests() {
        System.out.println("Running tests...");
        assertEquals("makeReadable(0)", "00:00:00", HumanReadableTime.makeReadable(0));
        assertEquals("makeReadable(59)", "00:00:59", HumanReadableTime.makeReadable(59));
        assertEquals("makeReadable(60)", "00:01:00", HumanReadableTime.makeReadable(60));
        assertEquals("makeReadable(90)", "00:01:30", HumanReadableTime.makeReadable(90));
        assertEquals("makeReadable(3599)", "00:59:59", HumanReadableTime.makeReadable(3599));
        assertEquals("makeReadable(3600)", "01:00:00", HumanReadableTime.makeReadable(3600));
        assertEquals("makeReadable(45296)", "12:34:56", HumanReadableTime.makeReadable(45296));
        assertEquals("makeReadable(86399)", "23:59:59", HumanReadableTime.makeReadable(86399));
        assertEquals("makeReadable(86400)", "24:00:00", HumanReadableTime.makeReadable(86400));
        assertEquals("makeReadable(359999)", "99:59:59", HumanReadableTime.makeReadable(359999));
    }
}