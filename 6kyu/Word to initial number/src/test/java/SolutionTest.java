import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {

    @Test
    public void convert_test0() {
        int R = 10234567;
        String s = "CodeWars";

        assertEquals(R, Converter.convert(s));
    }

    @Test
    public void convert_test1() {
        int R = 1020;
        String s = "KATA";

        assertEquals(R, Converter.convert(s));
    }

    @Test
    public void convert_testBasic2() {
        int R = 11001201;
        String s = "AABBADBA";

        assertEquals(R, Converter.convert(s));
    }

    @Test
    public void convert_testBasic3() {
        int R = 0;
        String s = "";

        assertEquals(R, Converter.convert(s));
    }

    @Test
    public void convert_testBasic4() {
        int R = 1;
        String s = "W";

        assertEquals(R, Converter.convert(s));
    }

    @Test
    public void convert_testBasic5() {
        int R = 111;
        String s = "WWW";

        assertEquals(R, Converter.convert(s));
    }

}