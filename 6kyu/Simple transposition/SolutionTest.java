import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {
    @Test
    public void basicTest() {
        doTest("Sample text", "Sml etapetx");
        doTest("Simple transposition", "Sml rnpstoipetasoiin");
        doTest("All that glitters is not gold", "Alta ltesi o odl htgitr sntgl");
        doTest("The better part of valor is discretion", "Tebte ato ao sdsrtoh etrpr fvlri icein");
        doTest("Conscience does make cowards of us all", "Cncec osmk oad fu losinede aecwrso sal");
        doTest("Imagination is more important than knowledge", "Iaiaini oeipratta nwegmgnto smr motn hnkolde");
    }

    @Test
    public void randomTest() {
        for (int trial = 1; trial < 20; trial++) {
            String text = randomString();
            StringBuilder sb1 = new StringBuilder(), sb2 = new StringBuilder();
            for (int i = 0; i < text.length(); i++)
                (i % 2 == 0 ? sb1 : sb2).append(text.charAt(i));
            doTest(text, sb1.toString() + sb2.toString());
        }
    }

    private String randomString() {
        StringBuilder sb = new StringBuilder();
        for (int count = randomInt(10, 40); count > 0; count--) sb.append(randomLetter());
        return sb.toString();
    }

    private static final String letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ    ";

    private char randomLetter() {
        return letters.charAt(randomInt(0, letters.length() - 1));
    }

    private int randomInt(int min, int max) {
        return (int) (Math.random() * (max - min + 1) + min);
    }

    private void doTest(String text, String expected) {
        assertEquals(expected, Kata.simpleTransposition(text));
    }
}