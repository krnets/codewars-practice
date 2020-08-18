/*
You are given an array(list) strarr of strings and an integer k.
Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Example:

        longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2)
        --> "abigailtheta"

        n being the length of the string array,
        if n = 0 or k > n or k <= 0 return "".

Note: consecutive strings : follow one after another without an interruption
*/

/*
import java.util.ArrayList;

class LongestConsec {
    public static String longestConsec(String[] strarr, int k) {
        var list = new ArrayList<String>();
        int longest = 0;

        for (int i = 0; i < strarr.length - k + 1; i++) {
            var sb = new StringBuilder();

            for (int j = 0; j < k; j++) {
                sb.append(strarr[i + j]);
            }
            list.add(sb.toString());
            longest = Math.max(longest, sb.length());
        }
        for (String s : list) {
            if (s.length() == longest)
                return s;
        }
        return "";
    }
}
*/

/*
class LongestConsec {
    public static String longestConsec(String[] strarr, int k) {
        String longest = "";

        for (int i = 0; i < strarr.length - k + 1; i++) {
            var sb = new StringBuilder();

            for (int j = 0; j < k; j++)
                sb.append(strarr[i + j]);

            if (sb.length() > longest.length())
                longest = sb.toString();
        }
        return longest;
    }
}
*/

import static java.util.Arrays.stream;
import static java.util.Comparator.comparing;
import static java.util.stream.Collectors.joining;
import static java.util.stream.IntStream.rangeClosed;

class LongestConsec {
    public static String longestConsec(String[] strarr, int k) {
        return k < 0 ? "" : rangeClosed(0, strarr.length - k)
                .mapToObj(i -> stream(strarr, i, i + k).collect(joining()))
                .max(comparing(String::length))
                .orElse("");
    }
}
