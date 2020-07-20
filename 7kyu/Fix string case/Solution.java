/*
In this Kata, you will be given a string that may have mixed uppercase and lowercase letters
and your task is to convert that string to either lowercase only or uppercase only based on:

        make as few changes as possible.
        if the string contains equal number of uppercase and lowercase letters,
        convert the string to lowercase.

        For example:

        solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
        solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
        solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
*/

/*
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static java.lang.Character.*;

public class Solution {
    public static String solve(final String str) {
        int countUpper = 0;
        int countLower = 0;
        char[] chars = str.toCharArray();

        for (char c : chars) {
            if (isUpperCase(c)) countUpper++;
            else countLower++;
        }
        if (countLower < countUpper) {
            for (int i = 0; i < chars.length; i++)
                if (isLowerCase(chars[i]))
                    chars[i] = toUpperCase(chars[i]);
        }
        if (countLower > countUpper) {
            for (int i = 0; i < chars.length; i++)
                if (isUpperCase(chars[i]))
                    chars[i] = toLowerCase(chars[i]);
        }
        return countLower == countUpper ? str.toLowerCase() :
                Stream.of(chars).map(String::valueOf).collect(Collectors.joining());
    }
}*/

/*
public class Solution {
    public static String solve(final String str) {
        return str.chars().filter(Character::isUpperCase).count() >= str.chars().filter(Character::isLowerCase).count() ?
                str.toUpperCase() : str.toLowerCase();
    }
}
*/
/*

public class Solution {
    public static String solve(final String str) {
        int lenUpper = str.replaceAll("[a-z]", "").length();
        int lenLower = str.replaceAll("[A-Z]", "").length();
        return lenUpper > lenLower ? str.toUpperCase() : str.toLowerCase();
    }
}*/

public class Solution {
    public static String solve(final String str) {
        int lenLower = str.replaceAll("[A-Z]", "").length();
        return lenLower < str.length() - lenLower ? str.toUpperCase() : str.toLowerCase();
    }
}
