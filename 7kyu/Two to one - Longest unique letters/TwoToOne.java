/*
Take 2 strings s1 and s2 including only letters from ato z.
Return a new sorted string, the longest possible, containing distinct letters,
each taken only once - coming from s1 or s2.

        a = "xyaabbbccccdefww"
        b = "xxxxyyyyabklmopq"
        longest(a, b) -> "abcdefklmopqwxy"

        a = "abcdefghijklmnopqrstuvwxyz"
        longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
*/


import java.util.stream.Collectors;
import java.util.stream.Stream;

public class TwoToOne {
    public static String longest(String s1, String s2) {
        return Stream.of(s1.concat(s2).split(""))
                .distinct()
                .sorted()
                .collect(Collectors.joining());
    }
}