import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {

    @Test
    public void basicTest1() {
        assertEquals(0, Trumpdetector.detect("I will build a huge wall"), 0.001);
    }

    @Test
    public void basicTest2() {
        assertEquals(4, Trumpdetector.detect("HUUUUUGEEEE WAAAAAALL"), 0.001);
    }

    @Test
    public void basicTest3() {
        assertEquals(2.5, Trumpdetector.detect("MEXICAAAAAAAANS GOOOO HOOOMEEEE"), 0.001);
    }

    @Test
    public void basicTest4() {
        assertEquals(1.89, Trumpdetector.detect("America NUUUUUKEEEE Oooobaaaamaaaaa"), 0.001);
    }

    @Test
    public void basicTest5() {
        assertEquals(1.56, Trumpdetector.detect("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT"), 0.001);
    }
}
