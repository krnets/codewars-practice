/*
Write a method that will search an array of strings for all strings that contain another string,
ignoring capitalization. Then return an array of the found strings.

The method takes two parameters, the query string and the array of strings to search, and returns an array.

If the string isn't contained in any of the strings in the array, the method returns an array
containing a single string: "Empty"

Examples

If the string to search for is "me", and the array to search is ["home", "milk", "Mercury", "fish"],
the method should return ["home", "Mercury"].
*/

import java.util.Arrays;

/*
public class WordSearch {
    static String[] findWord(String x, String[] y) {
        var results = Arrays.stream(y).filter(s -> s.toLowerCase().contains(x)).toArray(String[]::new);
        return results.length > 0 ? results : new String[]{"Empty"};
    }
}
*/

public class WordSearch {
    static String[] findWord(String x, String[] y) {
        return x.trim().isEmpty() ? new String[]{"Empty"} :
                Arrays.stream(y).filter(s -> s.toLowerCase().contains(x)).toArray(String[]::new);
    }
}
