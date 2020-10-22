/*
Move the first letter of each word to the end of it,
then add "ay" to the end of the word.
Leave punctuation marks untouched.

        pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
        pigIt('Hello world !');     // elloHay orldway !
*/

import java.util.Arrays;
import java.util.stream.Collectors;

public class PigLatin {
    public static String pigIt(String str) {
        return Arrays.stream(str.split(" "))
                .map(x -> Character.isLetter(x.charAt(0)) ? x.substring(1) + x.charAt(0) + "ay" : x)
                .collect(Collectors.joining(" "));
    }
}

/*
public class PigLatin {
    public static String pigIt(String str) {
        return str.replaceAll("(\\w)(\\w*)", "$2$1ay");
    }
}
*/

/*
import java.util.ArrayList;

public class PigLatin {
    public static String pigIt(String str) {
        var list = new ArrayList<String>();

        for (String s : str.split(" ")) {
            String sb = s.substring(1) + s.charAt(0) + (Character.isLetter(s.charAt(0)) ? "ay" : "");
            list.add(sb);
        }
        return String.join(" ", list);
    }
}
*/
