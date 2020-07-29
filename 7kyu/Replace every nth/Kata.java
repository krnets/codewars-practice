/*
Write a method, that replaces every nth char oldValue with char newValue.

        replaceNth(String text, int n, char oldValue, char newValue)

Example:
        n:         2
        oldValue: 'a'
        newValue: 'o'
        "Vader said: No, I am your father!" -> "Vader soid: No, I am your fother!"
          1     2          3        4       -> 2nd and 4th occurence are replaced

        Your method has to be case sensitive.

        As you can see in the example: The first changed is the 2nd 'a'.
        So the start is always at the nth suitable char and not at the first!

        If n is 0 or negative or if it is larger than the count of the oldValue,
        return the original text without a change.

        The text and the chars will never be null.
*/


/*
public class Kata {
    public static String replaceNth(String text, int n, char oldValue, char newValue) {
        if (n == 0) return text;
        var chars = text.toCharArray();
        int trackValue = 0;
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == oldValue)
                trackValue++;
            if (trackValue == n) {
                chars[i] = newValue;
                trackValue = 0;
            }
        }
        return new String(chars);
    }
}
*/

import java.util.concurrent.atomic.AtomicInteger;

public class Kata {
    public static String replaceNth(String text, int n, char oldValue, char newValue) {
        var count = new AtomicInteger();
        return n < 1 ? text : text.chars()
                .map(c -> c == oldValue && count.incrementAndGet() % n == 0 ? newValue : c)
                .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append)
                .toString();
    }
}
