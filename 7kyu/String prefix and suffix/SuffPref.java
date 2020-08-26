/*
In this Kata, you will be given a string and your task will be to return the length
of the longest prefix that is also a suffix. A prefix is the start of a string
while the suffix is the end of a string. For instance, the prefixes of the string
"abcd" are ["a","ab","abc"]. The suffixes are ["bcd", "cd", "d"].

You should not overlap the prefix and suffix.

        for example:
        solve("abcd") = 0, because no prefix == suffix.
        solve("abcda") = 1, because the longest prefix which == suffix is "a".
        solve("abcdabc") = 3. Longest prefix which == suffix is "abc".
        solve("aaaa") = 2. Longest prefix which == suffix is "aa". You should not overlap the prefix and suffix
        solve("aa") = 1. You should not overlap the prefix and suffix.
        solve("a") = 0. You should not overlap the prefix and suffix.

        All strings will be lowercase and string lengths are 1 <= length <= 500

        More examples in test cases. Good luck!
*/

/*
import java.util.stream.IntStream;

public class SuffPref {
    public static int solve(String s) {
        return IntStream.iterate(s.length() / 2, i -> i > 0, i -> i - 1)
                .filter(i -> s.substring(0, i).equals(s.substring(s.length() - i)))
                .findFirst().orElse(0);
    }
}*/

public class SuffPref {
    public static int solve(String s) {
        for (int i = s.length() / 2; i >= 0; i--) {
            var prefix = s.substring(0, i);
            if (s.endsWith(prefix))
                return prefix.length();
        }
        return 0;
    }
}
