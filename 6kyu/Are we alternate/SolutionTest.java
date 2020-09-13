import java.util.Random;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class SolutionTest {
    @Test
    public void exampleTests() {
        assertEquals(true, Solution.isAlt("amazon"));
        assertEquals(false, Solution.isAlt("apple"));
        assertEquals(true, Solution.isAlt("banana"));
    }

    @Test
    public void randomTests() {
        Random r = new Random();
        for (int i = 0; i < 50; i++) {
            StringBuilder sb = new StringBuilder();

            for (int j = r.nextInt(10); j < 10 && sb.length() < 8; j++)
                if (r.nextBoolean()) //extra statement so that vowels appear more often
                    sb.append(nextVowel(r)).append(nextChar(r));
                else sb.append(nextChar(r));

            String word = sb.toString();
            System.out.println(word);

            assertEquals(isAlt(word), Solution.isAlt(word));
        }
    }

    private char nextVowel(Random r) {
        return "aeiou".charAt(r.nextInt(5));
    }

    private char nextChar(Random r) {
        return (char) (97 + r.nextInt(26));
    }

    private boolean isAlt(String word) {
        return !word.matches(".*[aeiou]{2}.*|.*[^aeiou]{2}.*");
    }
}