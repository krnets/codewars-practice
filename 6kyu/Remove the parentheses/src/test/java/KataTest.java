import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class KataTest {

    @Test
    public void test_BasicTest1() {
        assertEquals("exampleexample", Kata.removeParentheses("example(unwanted thing)example"));
    }

    @Test
    public void test_BasicTest2() {
        assertEquals("example  example", Kata.removeParentheses("example (unwanted thing) example"));
    }

    @Test
    public void test_BasicTest3() {
        assertEquals("a e", Kata.removeParentheses("a (bc d)e"));
    }

    @Test
    public void test_BasicTest4() {
        assertEquals("a", Kata.removeParentheses("a(b(c))"));
    }

    @Test
    public void test_BasicTest5() {
        assertEquals("hello example  something", Kata
                .removeParentheses("hello example (words(more words) here) something"));
    }

    @Test
    public void test_BasicTest6() {
        assertEquals("  ", Kata.removeParentheses("(first group) (second group) (third group)"));
    }
}