import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class SolutionTest {
    @Test
    public void testSomething() {
        assertEquals(true, new Solution().checkThreeAndTwo(new char[] { 'a', 'a', 'b', 'b', 'b' }));
        assertEquals(false, new Solution().checkThreeAndTwo(new char[] { 'a', 'c', 'a', 'c', 'b' }));
        assertEquals(false, new Solution().checkThreeAndTwo(new char[] { 'a', 'a', 'a', 'a', 'a' }));
    }
}