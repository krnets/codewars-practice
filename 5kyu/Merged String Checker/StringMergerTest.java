import org.junit.Test;

import java.util.Random;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;


public class StringMergerTest {

    private final Random random = new Random();


    @Test
    public void normalHappyFlow() {
        assertTrue("codewars can be created from code and wars", StringMerger.isMerge("codewars", "code", "wars"));
        assertTrue("codewars can be created from cdwr and oeas", StringMerger.isMerge("codewars", "cdwr", "oeas"));
        assertTrue("Making progress", StringMerger.isMerge("Making progress", "Mak pross", "inggre"));
    }

    @Test
    public void alwaysPass() {
        assertTrue("this can't fail", true);
    }

    @Test
    public void normalSadFlow() {
        assertFalse("codewars is not code + code", StringMerger.isMerge("codewars", "code", "code"));
        assertFalse("More progress", StringMerger.isMerge("More progress", "More ess", "pro"));
    }

    @Test
    public void canHandleEmptyPart() {
        assertTrue("codewars are codewars", StringMerger.isMerge("codewars", "codewars", ""));
        assertTrue("codewars are codewars", StringMerger.isMerge("codewars", "", "codewars"));
    }

    @Test
    public void canHandleTooFewChars() {
        assertFalse("codewars is not codewar", StringMerger.isMerge("codewars", "code", "war"));
        assertFalse("codewars is not co", StringMerger.isMerge("codewars", "c", "o"));
    }

    @Test
    public void canHandleExtraChars() {
        assertFalse("codewars is not codewarss", StringMerger.isMerge("codewars", "code", "warss"));
    }

    @Test
    public void canHandleCharactersInWrongOrder() {
        assertFalse("codewars can't be created from code and wasr", StringMerger.isMerge("codewars", "code", "wasr"));
        assertFalse("codewars can't be created from cwdr and oeas", StringMerger.isMerge("codewars", "cwdr", "oeas"));
    }

    @Test
    public void canHandleEmptyStrings() {
        assertFalse("empty result string", StringMerger.isMerge("", "code", "wars"));
        assertFalse("empty part one", StringMerger.isMerge("codewars", "", "code"));
        assertFalse("empty part two", StringMerger.isMerge("codewars", "code", ""));
        assertFalse("empty parts", StringMerger.isMerge("codewars", "", ""));
        assertTrue("all empty", StringMerger.isMerge("", "", ""));
    }

    @Test
    public void canHandleBananas() {
        assertTrue("Going bananas!", StringMerger.isMerge("Bananas from Bahamas", "Bahas", "Bananas from am"));
    }

    @Test
    public void someRandomCases() {
        for (int i = 0; i < 20; i++) {
            String[] parts = splitString("Can we merge it? Yes, we can!");
            if (random.nextBoolean())
                assertTrue("'Can we merge it? Yes, we can!' is a merge of '" +
                                parts[0] + "' and '" + parts[1] + "'",
                        StringMerger.isMerge("Can we merge it? Yes, we can!", parts[0], parts[1]));
            else
                assertFalse("'Can we merge it? No, we can't!' is a not merge of '" +
                                parts[0] + "' and '" + parts[1] + "'",
                        StringMerger.isMerge("Can we merge it? No, we can't!", parts[0], parts[1]));
        }
    }

    @Test
    public void someMoreRandomCases() {
        for (int i = 0; i < 20; i++) {
            String s = randomString();
            String[] parts = splitString(s);
            assertTrue("'" + s + "' is a merge of '" +
                            parts[0] + "' and '" + parts[1] + "'",
                    StringMerger.isMerge(s, parts[0], parts[1]));
        }
    }

    @Test
    public void evenMoreRandomCases() {
        for (int i = 0; i < 20; i++) {
            String s = randomString();
            if (random.nextBoolean() || s.charAt(0) == s.charAt(s.length() - 1)) {
                String[] parts = splitString(s);
                assertTrue("'" + s + "' is a merge of '" +
                                parts[0] + "' and '" + parts[1] + "'",
                        StringMerger.isMerge(s, parts[0], parts[1]));
            } else {
                String[] parts = splitString(s);
                s = s.charAt(s.length() - 1) + s.substring(1, s.length() - 1) + s.charAt(0);
                assertFalse("'" + s + "' is not a merge of '" +
                                parts[0] + "' and '" + parts[1] + "'",
                        StringMerger.isMerge(s, parts[0], parts[1]));
            }
        }
    }

    @Test
    public void someTrickyRandomCases() {
        for (int i = 0; i < 20; i++) {
            String[] chunks = {randomString(), randomString(),
                    randomString(), randomString()};
            String s = chunks[0] + chunks[1] + chunks[0] + chunks[2] + chunks[3];
            String p1 = chunks[0] + chunks[2];
            String p2 = chunks[0] + chunks[1] + chunks[3];
            assertTrue("'" + s + "' is a merge of '" +
                            p1 + "' and '" + p2 + "'",
                    StringMerger.isMerge(s, p1, p2));
        }
    }

    private String randomString() {
        StringBuilder s = new StringBuilder();
        int length = random.nextInt(20) + 10;
        for (int i = 0; i < length; i++) {
            char ch = (char) (random.nextInt(123 - 32) + 32);
            s.append(ch);
        }
        return s.toString();
    }

    private String[] splitString(String s) {
        StringBuilder s1 = new StringBuilder();
        StringBuilder s2 = new StringBuilder();
        for (char ch : s.toCharArray()) {
            if (random.nextBoolean())
                s1.append(ch);
            else
                s2.append(ch);
        }
        return new String[]{s1.toString(), s2.toString()};
    }


}