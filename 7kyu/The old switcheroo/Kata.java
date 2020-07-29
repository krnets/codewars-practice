/*
Write a function

        Kata.Vowel2Index("this is my string") == "th3s 6s my str15ng"
        Kata.Vowel2Index("Codewars is the best site in the world") ==
                         "C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld"

        Your function should be case insensitive to the vowels.
*/

import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Kata {
    public static String vowel2Index(String s) {
        return IntStream.range(0, s.length())
                .mapToObj(i -> (s.charAt(i) + "").matches("(?i)[aeiou]") ? (i + 1) + "" : s.charAt(i) + "")
                .collect(Collectors.joining());
    }
}
/*
public class Kata {
    public static String vowel2Index(String s) {
        return IntStream.range(0, s.length())
                .mapToObj(i -> String.valueOf(s.charAt(i)).matches("[aeiou]") ?
                        String.valueOf(i + 1) :
                        String.valueOf(s.charAt(i)))
                .collect(Collectors.joining());
    }
}
*/

/*
public class Kata {
    public static String vowel2Index(String s) {
        return IntStream.range(0, s.length())
                .mapToObj(i -> "aeiou".contains("" + s.charAt(i)) ? "" + (i + 1) : "" + s.charAt(i))
                .collect(Collectors.joining());
    }
}
*/
