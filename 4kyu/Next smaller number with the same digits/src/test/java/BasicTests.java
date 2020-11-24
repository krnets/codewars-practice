import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class BasicTests {

    @Test
    public void smallTest1() {
        assertEquals(12, Kata.nextSmaller(21));
    }

    @Test
    public void smallTest2() {
        assertEquals(790, Kata.nextSmaller(907));
    }

    @Test
    public void smallTest3() {
        assertEquals(513, Kata.nextSmaller(531));
    }

    @Test
    public void smallTest4() {
        assertEquals(-1, Kata.nextSmaller(1027));
    }

    @Test
    public void smallTest5() {
        assertEquals(414, Kata.nextSmaller(441));
    }

    @Test
    public void smallTest6() {
        assertEquals(123456789, Kata.nextSmaller(123456798));
    }
}