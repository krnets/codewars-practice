/*
When provided with a String, capitalize all vowels

        For example:

        Input : "Hello World!"

        Output : "HEllO WOrld!"

        Note: Y is not a vowel in this kata.
*/

/*
public class Kata {
    public static String swap(String st) {
        var chars = st.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (("" + chars[i]).matches("(?i)[aieou]"))
                chars[i] = (char) (chars[i] ^ 32);
        }
        return new String(chars);
    }
}*/

/*
public class Kata {
    public static String swap(String st) {
        var chars = st.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if ("aeiou".contains(String.valueOf(chars[i])))
                chars[i] = (char) (chars[i] - 32);
        }
        return new String(chars);
    }
}
*/

import java.util.Arrays;
import java.util.stream.Collectors;

public class Kata {
    public static String swap(String st) {
        return Arrays.stream(st.split(""))
                .map(c -> "aeiou".contains(c) ? c.toUpperCase() : c)
                .collect(Collectors.joining());
    }
}
