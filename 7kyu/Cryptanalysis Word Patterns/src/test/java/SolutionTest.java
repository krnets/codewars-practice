import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {

    @Test
    public void basicTest1() {
        assertEquals("0.1.2.2.3", Crypto.wordPattern("hello"));
    }

    @Test
    public void basicTest2() {
        assertEquals("0.1.2.2.3", Crypto.wordPattern("heLlo"));
    }

    @Test
    public void basicTest3() {
        assertEquals("0.1.2.2.3", Crypto.wordPattern("helLo"));
    }

    @Test
    public void basicTest4() {
        assertEquals(
                "0.1.2.2.3.2.3.4.3.5.3.6.7.4.8.3.7.9.7.10.11.1.2.2.9.12.13.14.1.3.2.0.3.15.1.13",
                Crypto.wordPattern("Hippopotomonstrosesquippedaliophobia"));
    }
}
