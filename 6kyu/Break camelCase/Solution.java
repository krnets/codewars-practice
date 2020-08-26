/*
Complete the solution so that the function will break up camel casing, using a space between words.

    solution("camelCasing")  ==  "camel Casing"
 */

import static java.lang.Character.isUpperCase;

/*
public class Solution {
    public static String camelCase(String input) {
        var sb = new StringBuilder();
        for (int i = 0; i < input.length(); i++) {
            var c = input.charAt(i);
            if (isUpperCase(c))
                sb.append(" ");
            sb.append(c);
        }
        return sb.toString();
    }
}
*/
/*class Solution {
    public static String camelCase(String input) {
        var sb = new StringBuilder();
        for (char c : input.toCharArray()) {
            if (isUpperCase(c))
                sb.append(" ");
            sb.append(c);
        }
        return sb.toString();
    }
}*/

/*
public class Solution {
    public static String camelCase(String input) {
        return input.replaceAll("([A-Z])", " $1");
    }
}
*/
public class Solution {
    public static String camelCase(String input) {
        var arr = input.split("(?=[A-Z])");
        return String.join(" ", arr);
    }
}
