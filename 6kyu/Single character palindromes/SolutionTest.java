import org.junit.Test;

import java.util.Random;

import static org.junit.Assert.assertEquals;

public class SolutionTest {
    private static Random random = new Random();

    private static boolean pals(String s, int lo, int hi) {
        while (lo < hi) {
            if (s.charAt(lo) != s.charAt(hi)) return false;
            lo++;
            hi--;
        }
        return true;
    }

    public static String bye(String s) {
        int lo = 0, hi = s.length() - 1;
        while (lo < hi) {
            if (s.charAt(lo) == s.charAt(hi)) {
                lo++;
                hi--;
            } else {
                if (pals(s, lo + 1, hi) || pals(s, lo, hi - 1))
                    return "remove one";
                return "not possible";
            }
        }
        return "OK";
    }

    private static int random(int l, int u) {
        return random.nextInt(u - l) + l;
    }

    @Test
    public void basicTests() {

        assertEquals("OK", Solution.solve("abba"));
        assertEquals("remove one", Solution.solve("abbaa"));
        assertEquals("not possible", Solution.solve("abbaab"));
        assertEquals("remove one", Solution.solve("madmam"));
        assertEquals("not possible", Solution.solve("raydarm"));
        assertEquals("OK", Solution.solve("hannah"));
    }

    @Test
    public void edgeCases() {

        assertEquals("remove one", Solution.solve("baba"));
        assertEquals("OK", Solution.solve("babab"));
        assertEquals("remove one", Solution.solve("bababa"));
        assertEquals("remove one", Solution.solve("abcbad"));
        assertEquals("remove one", Solution.solve("abcdba"));
        assertEquals("remove one", Solution.solve("dabcba"));
        assertEquals("remove one", Solution.solve("abededba"));
        assertEquals("remove one", Solution.solve("abdcdeba"));
        assertEquals("remove one", Solution.solve("abcdedba"));
        assertEquals("not possible", Solution.solve("abbcdedba"));
    }

    @Test
    public void randomTests() {
        String[] palns = new String[]{"racecar", "onino", "anna", "ana", "alula", "murdrum", "wesew", "boob", "birdrib", "babybab", "camac", "civic", "campmac", "deified", "deleveled", "devoved", "dewed", "detartrated", "diallaid", "dontnod", "drawward", "dumbmud", "drawnonward", "elle", "eve", "evilolive", "evitative", "godog", "hanah", "hannah", "ipreferpi", "kayak", "kahak", "kanakanak", "kinikinik", "lemel", "level", "lionoil", "liveevil", "madam", "minim", "mirrorim", "mom", "mygym", "nattan", "noon", "nursesrun", "pottop", "refer", "reifier", "repaper", "rotator", "roravator", "rotor", "radar", "sagas", "sexes", "solos", "stats", "tenet", "terret", "testset", "toidiot", "topspot"};
        String letters = "abcdefghijklmnopqrstuvwxyzab";
        int len = palns.length - 1;
        for (int i = 0; i < 250; i++) {
            String s = palns[random(0, len)];
            int jump = random(0, 10);
            if (jump <= 6) {
                int idx = random(0, s.length() - 1);
                s = s.substring(0, idx) + letters.charAt(random(0, 26)) + s.substring(idx, s.length());
                int b = random(0, 5);
                if (b <= 2) {
                    idx = random(0, s.length() - 1);
                    s = s.substring(0, idx) + letters.charAt(random(0, 26)) + s.substring(idx, s.length());
                }
            }
            assertEquals(bye(s), Solution.solve(s));
        }
    }
}