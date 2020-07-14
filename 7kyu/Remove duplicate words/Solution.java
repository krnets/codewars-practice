/*
Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

        Input:
        'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

        Output:
        'alpha beta gamma delta'
*/

import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Solution {
    public static String removeDuplicateWords(String s) {
        return Stream.of(s.split(" "))
                .distinct()
                .collect(Collectors.joining(" "));
    }
}