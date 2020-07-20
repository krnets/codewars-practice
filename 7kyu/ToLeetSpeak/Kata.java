/*
Your task is to write a function toLeetSpeak that converts a regular english sentence to Leetspeak.

More about LeetSpeak You can read at wiki -> https://en.wikipedia.org/wiki/Leet

Consider only uppercase letters (no lowercase letters, no numbers) and spaces.

        For example:

        toLeetSpeak("LEET") returns "1337"

        In this kata we use a simple LeetSpeak dialect. Use this alphabet:

        {
        A : '@',
        B : '8',
        C : '(',
        D : 'D',
        E : '3',
        F : 'F',
        G : '6',
        H : '#',
        I : '!',
        J : 'J',
        K : 'K',
        L : '1',
        M : 'M',
        N : 'N',
        O : '0',
        P : 'P',
        Q : 'Q',
        R : 'R',
        S : '$',
        T : '7',
        U : 'U',
        V : 'V',
        W : 'W',
        X : 'X',
        Y : 'Y',
        Z : '2'
        }
*/

import java.util.HashMap;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/*
public class Kata {
    public static String toLeetSpeak(final String speak) {
        var leetSpeak = new HashMap<String, String>();
        leetSpeak.put("A", "@");
        leetSpeak.put("B", "8");
        leetSpeak.put("C", "(");
        leetSpeak.put("E", "3");
        leetSpeak.put("G", "6");
        leetSpeak.put("H", "#");
        leetSpeak.put("I", "!");
        leetSpeak.put("L", "1");
        leetSpeak.put("O", "0");
        leetSpeak.put("S", "$");
        leetSpeak.put("T", "7");
        leetSpeak.put("Z", "2");

        return Stream.of(speak.split(""))
                .map(v -> leetSpeak.getOrDefault(v, v))
                .collect(Collectors.joining());
    }
}
*/

public class Kata {
    public static String toLeetSpeak(final String speak) {
        var leetSpeak = new HashMap<String, String>();
        var pairs = new String[]{
                "A", "@",
                "B", "8",
                "C", "(",
                "E", "3",
                "G", "6",
                "H", "#",
                "I", "!",
                "L", "1",
                "O", "0",
                "S", "$",
                "T", "7",
                "Z", "2"};

        for (int i = 0; i < pairs.length; i += 2) {
            String k = pairs[i];
            String v = pairs[i + 1];
            leetSpeak.put(k, v);
        }
        return Stream.of(speak.split(""))
                .map(v -> leetSpeak.getOrDefault(v, v))
                .collect(Collectors.joining());
    }
}
