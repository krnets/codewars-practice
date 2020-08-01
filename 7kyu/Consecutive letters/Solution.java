/*
In this Kata, we will check if a string contains consecutive letters as they appear in the English alphabet
and if each letter occurs only once.

Rules are: (1) the letters are adjacent in the English alphabet, and (2) each letter occurs only once.

For example:
        solve("abc") = True, because it contains a,b,c
        solve("abd") = False, because a, b, d are not consecutive/adjacent in the alphabet, and c is missing.
        solve("dabc") = True, because it contains a, b, c, d
        solve("abbc") = False, because b does not occur once.
        solve("v") = True

All inputs will be lowercase letters.
*/

/*
import java.util.Arrays;
import java.util.stream.IntStream;

public class Solution {
    public static boolean solve(String s) {
        var chars = s.toCharArray();
        Arrays.sort(chars);
        return s.length() == 1 || IntStream.range(1, chars.length)
                .allMatch(i -> (int) chars[i] - chars[i - 1] == 1);
    }
}*/

import static java.lang.Character.getNumericValue;

public class Solution {
    public static boolean solve(String s) {
        return getNumericValue(s.chars().max().orElse(0)) -
                getNumericValue(s.chars().min().orElse(0)) + 1 == s.length()
                && s.length() == s.chars().distinct().count();
    }
}

/*
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution {
    public static boolean solve(String s) {
        return IntStream.range(0, 26)
                .mapToObj(i -> String.valueOf('a' + i))
                .collect(Collectors.joining())
                .contains(s.chars()
                        .sorted()
                        .mapToObj(String::valueOf)
                        .collect(Collectors.joining()));
    }
}
*/
