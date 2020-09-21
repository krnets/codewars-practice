import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class Lucas_test {
    @Test
    public void test_lucasnum() throws Exception {
        assertEquals(1860498, Lucas.lucasnum(-30));
        assertEquals(-1149851, Lucas.lucasnum(-29));
        assertEquals(123, Lucas.lucasnum(-10));
        assertEquals(-76, Lucas.lucasnum(-9));
        assertEquals(47, Lucas.lucasnum(-8));
        assertEquals(-29, Lucas.lucasnum(-7));
        assertEquals(18, Lucas.lucasnum(-6));
        assertEquals(-11, Lucas.lucasnum(-5));
        assertEquals(7, Lucas.lucasnum(-4));
        assertEquals(-4, Lucas.lucasnum(-3));
        assertEquals(3, Lucas.lucasnum(-2));
        assertEquals(-1, Lucas.lucasnum(-1));
        assertEquals(2, Lucas.lucasnum(0));
        assertEquals(1, Lucas.lucasnum(1));
        assertEquals(3, Lucas.lucasnum(2));
        assertEquals(4, Lucas.lucasnum(3));
        assertEquals(7, Lucas.lucasnum(4));
        assertEquals(11, Lucas.lucasnum(5));
        assertEquals(18, Lucas.lucasnum(6));
        assertEquals(29, Lucas.lucasnum(7));
        assertEquals(47, Lucas.lucasnum(8));
        assertEquals(76, Lucas.lucasnum(9));
        assertEquals(123, Lucas.lucasnum(10));
        assertEquals(199, Lucas.lucasnum(11));
        assertEquals(322, Lucas.lucasnum(12));
        assertEquals(521, Lucas.lucasnum(13));
        assertEquals(843, Lucas.lucasnum(14));
        assertEquals(1364, Lucas.lucasnum(15));
    }
}