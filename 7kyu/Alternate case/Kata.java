/*
Write function alternateCase which switch every letter in string from upper to lower
and from lower to upper. E.g: Hello World -> hELLO wORLD
*/

import java.util.Arrays;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static java.lang.Character.isLetter;
import static java.lang.String.valueOf;
import static java.util.stream.Collectors.joining;

public class Kata {
    static String alternateCase(final String string) {
        var chars = string.toCharArray();
        for (int i = 0; i < chars.length; i++)
            if (isLetter(chars[i]))
                chars[i] = (char) (chars[i] ^ 32);
        return new String(chars);
    }
}

/*
public class Kata {
    static String alternateCase(final String string) {
        return Arrays.stream(string.split(""))
                .map(ch -> ch.toUpperCase() == ch ? ch.toLowerCase() : ch.toUpperCase())
                .collect(Collectors.joining());
    }
}
*/

/*
public class Kata {
    static String alternateCase(final String string) {
        return Arrays.stream(string.split(""))
                .map(ch -> Character.isUpperCase(ch.charAt(0)) ? ch.toLowerCase() : ch.toUpperCase())
                .collect(Collectors.joining());
    }
}
*/
