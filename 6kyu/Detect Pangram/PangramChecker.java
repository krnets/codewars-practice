/*
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram.
Return True if it is, False if not.
Ignore numbers and punctuation.
*/

import java.util.stream.Collectors;
import java.util.stream.IntStream;

/*
public class PangramChecker {
    public boolean check(String sentence) {
        return IntStream.range(0, 26)
                .mapToObj(i -> 'a' + i)
                .map(Character::toString)
                .collect(Collectors.joining())
                .equals(sentence
                        .toLowerCase()
                        .replaceAll("[^a-z]", "")
                        .chars()
                        .distinct()
                        .boxed()
                        .map(Character::toString)
                        .sorted()
                        .collect(Collectors.joining()));
    }
}
*/

/*
public class PangramChecker {
    public boolean check(String sentence) {
        return sentence.chars().boxed()
                .map(Character::toLowerCase)
                .filter(Character::isAlphabetic)
                .distinct().count() == 26;
    }
}
*/

public class PangramChecker {
    public boolean check(String sentence) {
        return sentence.toLowerCase().chars().boxed().filter(Character::isAlphabetic).distinct().count() == 26;
    }
}

/*
public class PangramChecker {
    public boolean check(String sentence) {
        sentence = sentence.toLowerCase();
        for (char c = 'a'; c <= 'z'; c++)
            if (sentence.indexOf(c) < 0)
                return false;
        return true;
    }
}
*/
