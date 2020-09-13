/*
Complete the method so that it formats the words into a single comma separated value.
The last word should be separated by the word 'and' instead of a comma.
The method takes in an array of strings and returns a single formatted string.

Empty string values should be ignored.

Empty arrays or null/nil values being passed into the method
should result in an empty string being returned.

        Kata.formatWords(new String[] {"ninja", "samurai", "ronin"}) => "ninja, samurai and ronin"
        Kata.formatWords(new String[] {"ninja", "", "ronin"}) => "ninja and ronin"
        Kata.formatWords(new String[] {}) => ""
*/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static java.util.Arrays.stream;
import static java.util.function.Predicate.not;
import static java.util.stream.Collectors.collectingAndThen;
import static java.util.stream.Collectors.joining;

/*
public class Kata {
    public static String formatWords(String[] words) {
        if (words == null)
            return "";

        return Arrays.stream(words)
                .filter(word -> word.length() > 0)
                .collect(Collectors.joining(", "))
                .replaceAll(",(?= [^,]*$)", " and");
    }
}*/

public class Kata {
    public static String formatWords(String[] words) {
        if (words == null)
            return "";

        return stream(words)
                .filter(not(String::isEmpty))
                .collect(collectingAndThen(joining(", "),
                        s -> s.replaceAll(", ([^,]+)$", " and $1")));
    }
}

/*
public class Kata {
    public static String formatWords(String[] words) {
        if (words == null)
            return "";

        List<String> clearWords = new ArrayList<>(Arrays.asList(words));
        clearWords.removeIf(String::isEmpty);

        if (clearWords.isEmpty())
            return "";

        if (clearWords.size() == 1)
            return clearWords.get(0);

        String allButLast = String.join(", ", clearWords.subList(0, clearWords.size() - 1));

        return allButLast + " and " + clearWords.get(clearWords.size() - 1);
    }
}
*/
