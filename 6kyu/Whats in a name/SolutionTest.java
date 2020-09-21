import org.junit.Test;

import static org.junit.Assert.assertEquals;

import org.junit.runners.JUnit4;

public class SolutionTest {
    @Test
    public void sampleTest() {
        assertEquals(Kata.nameInStr("Across the rivers", "chris"), true);
        assertEquals(Kata.nameInStr("Next to a lake", "chris"), false);
        assertEquals(Kata.nameInStr("Under a sea", "chris"), false);
        assertEquals(Kata.nameInStr("A crew that boards the ship", "chris"), false);
        assertEquals(Kata.nameInStr("A live son", "Allison"), false);
    }

    @Test
    public void randomTest() {
        String[] table = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ".split("");

        for (int i = 0; i < 20; ++i) {
            StringBuffer name = new StringBuffer();
            StringBuffer str = new StringBuffer();

            int leng = (int) (Math.random() * 2) + 5;

            for (int j = 0; j < leng; ++j) {
                name.append(table[(int) (Math.random() * table.length)]);
            }
            int leng2 = (int) (Math.random() * 5) + leng;

            for (int j = 0; j < leng2; ++j) {
                str.append(table[(int) (Math.random() * table.length)]);
            }

            assertEquals(Kata.nameInStr(str.toString(), name.toString()),
                    mySolution(str.toString(), name.toString()));
        }
    }

    private static boolean mySolution(String str, String name) {
        name = "^" + name.toLowerCase() + "$";
        name = String.join(".*?", name.split(""));
        return str.toLowerCase().matches(name);
    }
}