/*
Compare two strings by comparing the sum of their values (ASCII character code).

        For comparing treat all letters as UpperCase
        null/NULL/Nil/None should be treated as empty strings
        If the string contains other characters than letters, treat the whole string as it would be empty

        Your method should return true, if the strings are equal and false if they are not equal.
        Examples:

        "AD", "BC"  -> equal
        "AD", "DD"  -> not equal
        "gf", "FG"  -> equal
        "zz1", ""   -> equal (both are considered empty)
        "ZzZz", "ffPFF" -> equal
        "kl", "lz"  -> not equal
        null, ""    -> equal
*/


/*
public class Kata {
    public static boolean compare(String s1, String s2) {
        if (s1 == null || s2 == null
                || s1.replaceAll("[^A-Za-z]", "").equals("")
                || s2.replaceAll("[^A-Za-z]", "").equals(""))
            return true;
        return s1.toUpperCase().chars().sum() == s2.toUpperCase().chars().sum();
    }
}
*/

public class Kata {
    public static boolean compare(String s1, String s2) {
        if (s1 == null || s2 == null || !s1.matches("[A-Za-z]+") || !s2.matches("[A-Za-z]+"))
            return true;
        return s1.toUpperCase().chars().sum() == s2.toUpperCase().chars().sum();
    }
}
