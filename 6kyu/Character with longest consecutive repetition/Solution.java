/*
For a given string s find the character c (or C)
with longest consecutive repetition and return:

        Object[]{c, l};

        where l (or L) is the length of the repetition.
        If there are two or more characters with the same l
        return the first in order of appearance.

        For empty string return:

        Object[]{"", 0}
*/


/*
public class Solution {
    public static Object[] longestRepetition(String s) {
        if (s.isEmpty()) return new Object[]{"", 0};

        char current = s.charAt(0);
        char longest = current;

        int nCurrent = 0;
        int nLongest = 0;

        for (char c : s.toCharArray()) {
            if (current == c) {
                nCurrent++;
                if (nCurrent > nLongest) {
                    longest = c;
                }
            } else {
                nCurrent = 1;
            }
            if (nCurrent > nLongest) {
                nLongest = nCurrent;
            }
            current = c;
        }
        return new Object[]{String.valueOf(longest), nLongest};
    }
}
*/

import java.util.regex.Pattern;

public class Solution {
    public static Object[] longestRepetition(String s) {
        var regExp = Pattern.compile("(.)(\\1+)").matcher(s);
        var maxChar = "";
        int maxLength = 0;

        while (regExp.find()) {
            if (regExp.group().length() > maxLength) {
                maxChar = regExp.group().substring(0, 1);
                maxLength = regExp.group().length();
            }
        }
        return new Object[]{maxChar, maxLength};
    }
}
