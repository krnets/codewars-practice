import org.junit.Test;

public class SampleTest {
    @Test
    public void checkSmallValues() {
        Preloaded.doTest(69, true);
        Preloaded.doTest(8, false);
        Preloaded.doTest(57, true);
        Preloaded.doTest(6, true);
        Preloaded.doTest(13, true);
        Preloaded.doTest(16, false);
        Preloaded.doTest(91, true);
    }

    @Test
    public void checkMediumValues() {
        Preloaded.doTest(522, true);
        Preloaded.doTest(974, true);
        Preloaded.doTest(755, true);
        Preloaded.doTest(512, false);
        Preloaded.doTest(739, true);
        Preloaded.doTest(1006, true);
        Preloaded.doTest(838, true);
    }

    @Test
    public void checkLargeValues() {
        Preloaded.doTest(382131, true);
        Preloaded.doTest(118070, true);
        Preloaded.doTest(17209, true);
        Preloaded.doTest(32768, false);
        Preloaded.doTest(161997, true);
        Preloaded.doTest(400779, true);
        Preloaded.doTest(198331, true);
    }
}