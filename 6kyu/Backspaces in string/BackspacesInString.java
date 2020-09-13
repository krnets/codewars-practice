/*
Assume "#" is like a backspace in string.
This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.

Examples

        "abc#d##c"      ==>  "ac"
        "abc##d######"  ==>  ""
        "#######"       ==>  ""
        ""              ==>  ""
*/

/*
import java.util.Stack;
import java.util.stream.Collectors;

public class BackspacesInString {
    public String cleanString(String s) {
        var stack = new Stack<Character>();

        for (char c : s.toCharArray()) {
            if (c == '#' && stack.size() > 0)
                stack.pop();
            else stack.push(c);
        }
        return stack.stream()
                .map(String::valueOf)
                .filter(c -> !c.equals("#"))
                .collect(Collectors.joining());
    }
}
*/

public class BackspacesInString {
    public String cleanString(String s) {
        var sb = new StringBuilder(s);
        for (int i = 0; i < sb.length(); i++) {
            if (sb.charAt(i) == '#') {
                sb.deleteCharAt(i);
                if (i != 0) {
                    sb.deleteCharAt(i - 1);
                    i--;
                }
                i--;
            }
        }
        return sb.toString();
    }
}

/*
public class BackspacesInString {
    public String cleanString(String s) {
        int backspaceIdx = s.indexOf("#");

        if (backspaceIdx == -1) {
            return s;
        }
        if (backspaceIdx == 0) {
            return cleanString(s.substring(1));
        }
        return cleanString(s.substring(0, backspaceIdx - 1) + s.substring(backspaceIdx + 1));
    }
}
*/
