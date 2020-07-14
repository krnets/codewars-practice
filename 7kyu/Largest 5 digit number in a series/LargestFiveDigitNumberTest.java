import org.junit.Test;

import static org.junit.Assert.assertEquals;


public class LargestFiveDigitNumberTest {

    @Test
    public void test1() {
        assertEquals(83910, LargestFiveDigitNumber.solve("283910"));
    }

    @Test
    public void test2() {
        assertEquals(67890, LargestFiveDigitNumber.solve("1234567890"));
    }
}