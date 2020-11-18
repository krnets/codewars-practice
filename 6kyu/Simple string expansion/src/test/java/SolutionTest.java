import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {

    @Test
    public void basicTest1() {
        assertEquals("ababab", Solution.solve("3(ab)"));
    }

    @Test
    public void basicTest2() {
        assertEquals("abbbabbb", Solution.solve("2(a3(b))"));
    }

    @Test
    public void basicTest3() {
        assertEquals("bcc", Solution.solve("b(2(c))"));
    }

    @Test
    public void basicTest4() {
        assertEquals("bccbccbcc", Solution.solve("3(b(2(c)))"));
    }

    @Test
    public void basicTest5() {
        assertEquals("kabaccbaccbacc", Solution.solve("k(a3(b(a2(c))))"));
    }
}