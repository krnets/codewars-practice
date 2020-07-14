/*
An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

        Note: anagrams are case insensitive

        Complete the function to return true if the two arguments given are anagrams of each other;
        return false otherwise.

        "foefet" is an anagram of "toffee"

        "Buckethead" is an anagram of "DeathCubeK"
*/

import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/*
public class Kata {
    public static boolean isAnagram(String test, String original) {
        if (test == null || original == null || test.length() != original.length()) return false;
        var testArr = test.toLowerCase().toCharArray();
        var origArr = original.toLowerCase().toCharArray();
        Arrays.sort(testArr);
        Arrays.sort(origArr);
        return Arrays.equals(testArr, origArr);
    }
}
*/

/*
public class Kata {
    public static boolean isAnagram(String test, String original) {
        if (test == null || original == null || test.length() != original.length()) return false;
        return Stream.of(test.toLowerCase().split("")).sorted().collect(Collectors.joining()).equals(
                Stream.of(original.toLowerCase().split("")).sorted().collect(Collectors.joining()));
    }
}
*/
public class Kata {
    public static boolean isAnagram(String test, String original) {
        if (test == null || original == null || test.length() != original.length())
            return false;

        return Arrays.equals(
                Stream.of(test.toLowerCase().split("")).sorted().toArray(),
                Stream.of(original.toLowerCase().split("")).sorted().toArray());
    }
}
