/*
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

        For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

        The input will be a lowercase string with no spaces.
*/

import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/*
public class Solution {
    public static String[] capitalize(String s) {
        String left = IntStream.range(0, s.length())
                .mapToObj(i -> i % 2 == 0 ? String.valueOf(s.charAt(i))
                        .toUpperCase() : String.valueOf(s.charAt(i))
                        .toLowerCase())
                .collect(Collectors.joining());
        String right = IntStream.range(0, s.length())
                .mapToObj(i -> i % 2 == 0 ? String.valueOf(s.charAt(i))
                        .toLowerCase() : String.valueOf(s.charAt(i))
                        .toUpperCase())
                .collect(Collectors.joining());

        return new String[]{left, right};
    }
}
*/

public class Solution {
    public static String[] capitalize(String s) {
        var left = new StringBuilder();
        var right = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (i % 2 == 0) {
                left.append(String.valueOf(s.charAt(i))
                        .toUpperCase());
                right.append(String.valueOf(s.charAt(i))
                        .toLowerCase());
            } else {
                left.append(String.valueOf(s.charAt(i))
                        .toLowerCase());
                right.append(String.valueOf(s.charAt(i))
                        .toUpperCase());
            }
        }
        return new String[]{left.toString(), right.toString()};
    }
}
