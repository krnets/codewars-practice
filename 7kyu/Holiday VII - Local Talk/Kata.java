/*
In Bali, as far as I can gather, when ex-pats speak to locals,
they basically insert the word 'Pak' as often as possible.
I am assured it means something like 'mate' or 'sir'
but that could be completely wrong.

Anyway, as some basic language education(??) this kata requires you
to turn any sentence provided (s) into ex-pat balinese waffle
by inserting the word 'pak' between every other word.

Pak should not be the first or last word.
Strings of just spaces should return an empty string.
*/

/*
import java.util.Arrays;
import java.util.stream.Collectors;

public class Kata {
    public static String pak(final String s) {
        if (s.matches("^\\s*$"))
            return "";

        var result = Arrays.stream(s.split(" "))
                .map(word -> word + " pak ")
                .collect(Collectors.joining());

        return result.substring(0, result.length() - 5);
    }
}*/

/*
public class Kata {
    public static String pak(final String s) {
        return s.replace(" ", " pak ");
    }
}

*/
public class Kata {
    public static String pak(final String s) {
        return String.join(" pak ", s.split(" "));
    }
}
