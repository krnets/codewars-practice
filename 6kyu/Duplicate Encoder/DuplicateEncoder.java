/*
The goal of this exercise is to convert a string to a new string where each character
in the new string is "(" if that character appears only once in the original string,
or ")" if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.

        "din"      =>  "((("
        "recede"   =>  "()()()"
        "Success"  =>  ")())())"
        "(( @"     =>  "))(("

Notes: Assertion messages may be unclear about what they display in some languages.
If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
*/

import static java.util.Arrays.stream;
import static java.util.stream.Collectors.*;

/*
public class DuplicateEncoder {
    static String encode(String word) {
        var charCount = word.toLowerCase().chars()
                .mapToObj(Character::toString)
                .collect(groupingBy(c -> c, counting()));

        return word.toLowerCase().chars()
                .mapToObj(Character::toString)
                .map(c -> charCount.get(c) > 1 ? ")" : "(")
                .collect(joining());
    }
}
*/
/*
public class DuplicateEncoder {
    static String encode(String word) {
        var charCount = stream(word.toLowerCase().split(""))
                .collect(groupingBy(c -> c, counting()));

        return stream(word.toLowerCase().split(""))
                .map(c -> charCount.get(c) > 1 ? ")" : "(")
                .collect(joining());
    }
}
*/

public class DuplicateEncoder {
    static String encode(String word) {
        word = word.toLowerCase();
        var sb = new StringBuilder();
        for (int i = 0; i < word.length(); ++i) {
            char c = word.charAt(i);
            if (word.indexOf(c) == word.lastIndexOf(c)) sb.append("(");
            else sb.append(")");
        }
        return sb.toString();
    }
}
