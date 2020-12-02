import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {

    @Test
    public void intToNegabinaryTestZero() {
        assertEquals("0", Kata.intToNegabinary(0));
    }

    @Test
    public void intToNegabinaryTest6() {
        assertEquals("11010", Kata.intToNegabinary(6));
    }

    @Test
    public void intToNegabinaryTest() {
        assertEquals("1110", Kata.intToNegabinary(-6));
        assertEquals("1111101", Kata.intToNegabinary(45));
        assertEquals("11010111", Kata.intToNegabinary(-45));
        assertEquals("1011000111111", Kata.intToNegabinary(4587));
        assertEquals("11001000010101", Kata.intToNegabinary(-4587));
        assertEquals("10000000000000011", Kata.intToNegabinary(65535));
        assertEquals("10000000000000000", Kata.intToNegabinary(65536));
        assertEquals("110000000000000000", Kata.intToNegabinary(-65536));
    }

    @Test
    public void negabinayToIntTestZero() {
        assertEquals(0, Kata.negabinaryToInt("0"));
    }

    @Test
    public void negabinayToIntTest6() {
        assertEquals(6, Kata.negabinaryToInt("11010"));
    }

    @Test
    public void negabinayToIntTest() {
        assertEquals(-6, Kata.negabinaryToInt("1110"));
        assertEquals(45, Kata.negabinaryToInt("1111101"));
        assertEquals(-45, Kata.negabinaryToInt("11010111"));
        assertEquals(4587, Kata.negabinaryToInt("1011000111111"));
        assertEquals(-4587, Kata.negabinaryToInt("11001000010101"));
        assertEquals(65535, Kata.negabinaryToInt("10000000000000011"));
        assertEquals(65536, Kata.negabinaryToInt("10000000000000000"));
        assertEquals(-65536, Kata.negabinaryToInt("110000000000000000"));
    }

}
