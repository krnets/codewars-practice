/*
Given an array of strings, reverse them and their order in such way that
their length stays the same as the length of the original inputs.

        Input:  {"I", "like", "big", "butts", "and", "I", "cannot", "lie!"}
        Output: {"!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"}
*/

/*
import java.util.ArrayList;

public class ArrayReverser {
    public static String[] reverse(String[] a) {
        var lengths = new ArrayList<Integer>();
        var merged = new StringBuilder();
        var result = new ArrayList<String>();

        for (String s : a) {
            lengths.add(s.length());
            merged.append(s);
        }
        String reversed = merged.reverse().toString();

        for (int i = 0, j = 0; i < reversed.length(); j++) {
            int len = lengths.get(j);
            result.add(reversed.substring(i, i + len));
            i += len;
        }
//        return result.toArray(String[]::new);
        return result.toArray(new String[0]);
    }
}
*/

public class ArrayReverser {
    public static String[] reverse(String[] a) {
        var reversed = new StringBuilder(String.join("", a)).reverse().toString();
        var b = new String[a.length];
        int i = 0, x = 0;
        for (String s : a) {
            b[x++] = reversed.substring(i, i += s.length());
        }
        return b;
    }
}