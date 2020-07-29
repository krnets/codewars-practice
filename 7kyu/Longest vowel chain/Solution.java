/*
The vowel substrings in the word codewarriors are o,e,a,io.
The longest of these has a length of 2.
Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces,
return the length of the longest vowel substring. Vowels are any of aeiou.
*/

/*
import java.util.Arrays;

public class Solution {
    public static int solve(String s) {
        String[] arr = s.replaceAll("[^aeiou]", " ").split(" ");
        return Arrays.stream(arr).mapToInt(String::length).reduce(Math::max).orElse(0);
    }
}*/

import java.util.Arrays;

public class Solution {
    public static int solve(String s) {
        return Arrays.stream(s.split("[^aeiou]")).mapToInt(String::length).max().orElse(0);
    }
}
