/*
You will be given an vector of string(s). You must sort it alphabetically
(case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.
*/

import java.util.Arrays;

/*
public class SortAndStar {
    public static String twoSort(String[] s) {
        Arrays.sort(s);
        String result = "";
        for (char c : s[0].toCharArray())
            result += c + "***";
        return result.substring(0, result.length() - 3);
    }
}*/
public class SortAndStar {
    public static String twoSort(String[] s) {
        Arrays.sort(s);
        return String.join("***", s[0].split(""));
    }
}
