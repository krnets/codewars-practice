/*
Sort the inner content of every word of a string in descending order.
The inner content is the content of a word without first and the last char.

Some examples:

        "sort the inner content in descending order" ->
        "srot the inner ctonnet in dsnnieedcg oredr"

        "wait for me" ->
        "wiat for me"

        "this kata is easy" ->
        "tihs ktaa is esay"

The string will never be null and will never be empty.
It will contain only lowercase-letters and whitespaces.
*/

import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.Collectors;

/*
public class Kata {
    public static String sortTheInnerContent(String words) {
        return Arrays.stream(words.split(" "))
                .map(word -> word.substring(0, 1) +
                        (word.length() > 3 ? sortMidChars(word) + word.charAt(word.length() - 1) : word.substring(1)))
                .collect(Collectors.joining(" "));
    }

    private static String sortMidChars(String word) {
        return word.substring(1, word.length() - 1).chars()
                .boxed()
                .sorted(Comparator.reverseOrder())
                .map(Character::toString)
                .collect(Collectors.joining());
    }
}
*/

public class Kata {
    public static String sortTheInnerContent(String words) {
        return Arrays.stream(words.split(" "))
                .map(word -> word.length() < 4 ? word :
                        word.charAt(0) + sortMidChars(word) + word.charAt(word.length() - 1))
                .collect(Collectors.joining(" "));
    }

    private static String sortMidChars(String word) {
        return word.substring(1, word.length() - 1).chars().boxed()
                .sorted(Comparator.reverseOrder())
                .map(Character::toString)
                .collect(Collectors.joining());
    }
}
