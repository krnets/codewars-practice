/*
You are given an input string.

For each symbol in the string if it's the first character occurrence,
replace it with a '1', else replace it with the amount of times you've already seen it.

But will your code be performant enough?

        Examples:

        input   =  "Hello, World!"
        result  =  "1112111121311"

        input   =  "aaaaaaaaaaaa"
        result  =  "123456789101112"

There might be some non-ascii characters in the string.

Note: there will be no int domain overflow (character occurrences will be less than 2 billion).
*/

/*
import java.util.HashMap;

public class JomoPipi {
    public static String numericals(String s) {
        var charFrequency = new HashMap<Character, Integer>();
        var sb = new StringBuilder();

        for (char c : s.toCharArray()) {
            int timesSeen = charFrequency.getOrDefault(c, 0);
            charFrequency.put(c, ++timesSeen);
            sb.append(timesSeen);
        }
        return sb.toString();
    }
}*/


public class JomoPipi {
    static String numericals(String s) {
        var charFrequency = new char[1032];

        return s.chars().map(i -> ++charFrequency[i])
                .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
                .toString();
    }
}