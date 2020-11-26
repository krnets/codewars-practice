import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class LcsTest {

    @Test
    public void basicTest1() {
        assertEquals("", Lcs.lcs("", ""));
    }

    @Test
    public void basicTest2() {
        assertEquals("", Lcs.lcs("abc", ""));
    }

    @Test
    public void basicTest3() {
        assertEquals("", Lcs.lcs("", "abc"));
    }

    @Test
    public void basicTest4() {
        assertEquals("", Lcs.lcs("a", "b"));
    }

    @Test
    public void basicTest5() {
        assertEquals("a", Lcs.lcs("a", "a"));
    }

    @Test
    public void basicTest6() {
        assertEquals("ac", Lcs.lcs("abc", "ac"));
    }

    @Test
    public void basicTest7() {
        assertEquals("abc", Lcs.lcs("abcdef", "abc"));
    }

    @Test
    public void basicTest8() {
        assertEquals("acf", Lcs.lcs("abcdef", "acf"));
    }

    @Test
    public void basicTest9() {
        assertEquals("nottest", Lcs.lcs("anothertest", "notatest"));
    }

    @Test
    public void basicTest10() {
        assertEquals("12356", Lcs.lcs("132535365", "123456789"));
    }

    @Test
    public void basicTest11() {
        assertEquals("final", Lcs.lcs("nothardlythefinaltest", "zzzfinallyzzz"));
    }

    @Test
    public void basicTest12() {
        assertEquals("acdefghijklmnoq", Lcs.lcs("abcdefghijklmnopq", "apcdefghijklmnobq"));
    }
}