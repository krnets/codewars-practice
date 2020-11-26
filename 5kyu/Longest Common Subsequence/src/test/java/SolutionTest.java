import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {

    @Test
    public void exampleTest1() {
        assertEquals("", Solution.lcs("a", "b"));
    }

    @Test
    public void exampleTest2() {
        assertEquals("abc", Solution.lcs("abcdef", "abc"));
    }

    @Test
    public void testSequence3() {
        assertEquals("", Solution.lcs("a", "b"));
    }

    @Test
    public void testSequence4() {
        assertEquals("a", Solution.lcs("a", "a"));
    }

    @Test
    public void testSequence5() {
        assertEquals("ac", Solution.lcs("abc", "ac"));
    }

    @Test
    public void testSequence6() {
        assertEquals("abc", Solution.lcs("abcdef", "abc"));
    }

    @Test
    public void testSequence7() {
        assertEquals("acf", Solution.lcs("abcdef", "acf"));
    }

    @Test
    public void testSequence8() {
        assertEquals("nottest", Solution.lcs("anothertest", "notatest"));
    }

    @Test
    public void testSequence9() {
        assertEquals("12356", Solution.lcs("132535365", "123456789"));
    }

    @Test
    public void testSequence10() {
        assertEquals("final", Solution.lcs("finaltest", "zzzfinallyzzz"));
    }
}