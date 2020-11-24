import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class ExtendedTests {

    @Test
    public void extendedTest1() {
        assertEquals(351, Kata.nextSmaller(513));
    }

    @Test
    public void extendedTest2() {
        assertEquals(315, Kata.nextSmaller(351));
    }

    @Test
    public void extendedTest3() {
        assertEquals(153, Kata.nextSmaller(315));
    }

    @Test
    public void extendedTest4() {
        assertEquals(135, Kata.nextSmaller(153));
    }

    @Test
    public void extendedTest5() {
        assertEquals(-1, Kata.nextSmaller(135));
    }

    @Test
    public void extendedTest6() {
        assertEquals(2017, Kata.nextSmaller(2071));
    }

    @Test
    public void extendedTest7() {
        assertEquals(1072, Kata.nextSmaller(1207));
    }

    @Test
    public void extendedTest8() {
        assertEquals(144, Kata.nextSmaller(414));
    }

    @Test
    public void extendedTest9() {
        assertEquals(-1, Kata.nextSmaller(100));

    }

    @Test
    public void extendedTest10() {
        assertEquals(-1, Kata.nextSmaller(123456789));
    }

    @Test
    public void extendedTest11() {
        assertEquals(20990, Kata.nextSmaller(29009));
    }

    @Test
    public void extendedTest12() {
        assertEquals(1234567890, Kata.nextSmaller(1234567908));
    }

    @Test
    public void extendedTest13() {
        assertEquals(-1, Kata.nextSmaller(9999999999L));
    }

    @Test
    public void extendedTest14() {
        assertEquals(59884848459853L, Kata.nextSmaller(59884848483559L));
    }

    @Test
    public void extendedTest15() {
        assertEquals(-1, Kata.nextSmaller(1023456789));
    }

    @Test
    public void extendedTest16() {
        assertEquals(51226262627551L, Kata.nextSmaller(51226262651257L));
    }

    @Test
    public void extendedTest17() {
        assertEquals(-1, Kata.nextSmaller(202233445566L));
    }

    @Test
    public void extendedTest18() {
        assertEquals(-1, Kata.nextSmaller(506789));
    }
}
