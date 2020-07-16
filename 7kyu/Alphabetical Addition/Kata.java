/*
Your task is to add up letters to one letter.

        The function will be given an array of single character Strings, each one being a letter to add.
        Notes:

        Letters will always be lowercase.
        Letters can overflow (see second to last example of the description)
        If no letters are given, the function should return 'z'

        Examples:

        addLetters("a", "b", "c") = "f"
        addLetters("a", "b") = "c"
        addLetters("z") = "z"
        addLetters("z", "a") = "a"
        addLetters("y", "c", "b") = "d" // notice the letters overflowing
        addLetters() = "z"
*/

import java.util.stream.*;

public class Kata {
    public static String addLetters(String... letters) {
        final int abcFirstLetter = 97;
        var alphabet = IntStream.range(0, 26)
                .mapToObj(i -> Character.toString((char) (i + abcFirstLetter)))
                .collect(Collectors.joining());
        var len = alphabet.length();
        var sum = Stream.of(letters).mapToInt(c -> alphabet.indexOf(c) + 1).sum();
        var letter = (sum + len - 1) % len;
        return String.valueOf(alphabet.charAt(letter));
    }
}
