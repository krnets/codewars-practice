import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;
import org.junit.runners.Suite;

import static java.util.Arrays.asList;

import static org.junit.Assert.assertEquals;

@RunWith(Suite.class)
@Suite.SuiteClasses({
        DictionaryTests.BerriesTest.class,
        DictionaryTests.LanguagesTest.class,
        DictionaryTests.CodewarsTest.class,
        DictionaryTests.NonWordTest.class,
})
public class DictionaryTests {

    public static List<Object[]> shuffledList(Object[][] objects) {
        ArrayList<Object[]> list = new ArrayList<>(asList(objects));
        Collections.shuffle(list);
        return list;
    }

    public static abstract class BaseTest {

        protected final Dictionary dict;
        protected final String term;
        protected final String expected;

        public BaseTest(Dictionary dictionary, String term, String expected) {
            this.dict = dictionary;
            this.term = term;
            this.expected = expected;
        }

        @Test
        public void test() {
            assertEquals(expected, dict.findMostSimilar(term));
        }

    }

    @RunWith(Parameterized.class)
    public static class BerriesTest extends BaseTest {

        public BerriesTest(Dictionary dictionary, String term, String expected) {
            super(dictionary, term, expected);
        }

        @Parameters(name = " {1} ")
        public static Collection<Object[]> data() {
            Dictionary dict = new Dictionary(new String[]{"cherry", "peach", "pineapple", "melon", "strawberry", "raspberry", "apple", "coconut", "banana"});
            return shuffledList(new Object[][]{
                    {dict, "strawbery", "strawberry"},
                    {dict, "berry", "cherry"},
                    {dict, "aple", "apple"},
            });
        }
    }

    @RunWith(Parameterized.class)
    public static class LanguagesTest extends BaseTest {

        public LanguagesTest(Dictionary dictionary, String term, String expected) {
            super(dictionary, term, expected);
        }

        @Parameters(name = " {1} ")
        public static Collection<Object[]> data() {
            Dictionary dict = new Dictionary(new String[]{"javascript", "java", "ruby", "php", "python", "coffeescript", "c", "cpp", "brainfuck"});
            return shuffledList(new Object[][]{
                    {dict, "heaven", "java"},
                    {dict, "javascript", "javascript"},
            });
        }
    }

    @RunWith(Parameterized.class)
    public static class CodewarsTest extends BaseTest {

        public CodewarsTest(Dictionary dictionary, String term, String expected) {
            super(dictionary, term, expected);
        }

        @Parameters(name = " {1} ")
        public static Collection<Object[]> data() {
            Dictionary dict = new Dictionary(new String[]{"stars", "mars", "wars", "codec", "code", "codewars"});
            return shuffledList(new Object[][]{
                    {dict, "coddwars", "codewars"},
            });
        }
    }

    @RunWith(Parameterized.class)
    public static class NonWordTest extends BaseTest {

        public NonWordTest(Dictionary dictionary, String term, String expected) {
            super(dictionary, term, expected);
        }

        @Parameters(name = " {1} ")
        public static Collection<Object[]> data() {
            Dictionary dict = new Dictionary(new String[]{"psaysnhfrrqgxwik", "pdyjrkaylryr", "lnjhrzfrosinb", "afirbipbmkamjzw", "loogviwcojxgvi", "iqkyztorburjgiudi", "cwhyyzaorpvtnlfr", "iroezmixmberfr", "jhjyasikwyufr", "tklquxrnhfiggb", "cpnqknjyviusknmte", "hwzsemiqxjwfk", "ntwmwwmicnjvhtt", "emvquxrvvlvwvsi", "sefsknopiffajor", "znystgvifufptxr", "xuwahveztwoor", "hrwuhmtxxvmygb", "karpscdigdvucfr", "xrgdgqfrldwk", "nnsoamjkrzgldi", "ljxzjjorwgb", "cfvruditwcxr", "eglanhfredaykxr", "fxjskybblljqr", "qifwqgdsijibor", "xikoctmrhpvi", "ajacizfrgxfumzpvi", "mhmkakybpczjbb", "vkholxrvjwisrk", "npyrgrpbdfqhhncdi", "pxyousorusjxxbt", "jcocndjkyb", "fxpvfhfrujjaifr", "hkldhadcxrjbmkmcdi", "hirldidcuzbyb", "ggcvrtxrtnafw", "tdvibqccxr", "osbednerciaai", "qojfrlhufr", "kqijoorfkejdcxr", "zqdrhpviqslik", "clxmqmiycvidiyr", "xffrkbdyjveb", "dyhxgviphoptak", "dihhiczkdwiofpr", "riyhpvimgaliuxr", "fgtrjakzlnaebxr", "ppctybxgtleipb", "ucxmdeudiycokfnb"});
            return shuffledList(new Object[][]{
                    {dict, "rkacypviuburk", "zqdrhpviqslik"},
            });
        }
    }

}
