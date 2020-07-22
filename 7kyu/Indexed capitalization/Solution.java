/*
Given a string and an array of integers representing indices, capitalize all letters at the given indices.

        For example:

        capitalize("abcdef",[1,2,5]) = "aBCdeF"
        capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.

        The input will be a lowercase string with no spaces and an array of digits.
*/

/*
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Solution {
    public static String capitalize(String s, int[] ind) {
        return IntStream.range(0, s.length())
                .mapToObj(i -> IntStream.of(ind).anyMatch(x -> x == i) ?
                        s.substring(i, i + 1).toUpperCase() : s .substring(i, i + 1))
                .collect(Collectors.joining());
    }
}
*/

/*
public class Solution {
    public static String capitalize(String s, int[] ind) {
        var result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            int finalI = i;
            if (IntStream.of(ind).anyMatch(x -> x == finalI))
                result.append(s.substring(i, i + 1).toUpperCase());
            else result.append(s, i, i + 1);
        }
        return result.toString();
    }
}
*/

public class Solution {
    public static String capitalize(String s, int[] ind) {
        var chars = s.toCharArray();
        for (int value : ind)
            if (value < s.length())
                chars[value] = Character.toUpperCase(chars[value]);
        return String.valueOf(chars);
    }
}
