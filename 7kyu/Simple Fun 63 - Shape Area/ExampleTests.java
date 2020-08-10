import static org.junit.Assert.*;

public class ExampleTests {
    @org.junit.Test
    public void exampleTests() {
        assertEquals(5, Kata.shapeArea(2));
        assertEquals(13, Kata.shapeArea(3));
        assertEquals(1, Kata.shapeArea(1));
        assertEquals(41, Kata.shapeArea(5));
    }
}