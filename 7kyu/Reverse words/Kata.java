/*
Complete the function that accepts a string parameter, and reverses each word in the string.
All spaces in the string should be retained.

        "This is an example!" ==> "sihT si na !elpmaxe"
        "double  spaces"      ==> "elbuod  secaps"
*/

import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/*
public class Kata {
    public static String reverseWords(final String original) {
        if (original.isBlank()) return original;

        return Arrays.stream(original.split(" "))
                .map(word -> new StringBuilder(word).reverse().toString())
                .collect(Collectors.joining(" "));
    }
}*/
public class Kata {
    public static String reverseWords(final String original) {
        return Stream.of(original.split(" ", original.length()))
                .map(word -> new StringBuilder(word).reverse().toString())
                .collect(Collectors.joining(" "));
    }
}
