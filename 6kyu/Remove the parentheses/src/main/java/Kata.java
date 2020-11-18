/*
public class Kata {
    public static String removeParentheses(final String str) {
        var sb = new StringBuilder();
        int depth = 0;

        for (char c : str.toCharArray()) {
            if (c == '(') depth++;
            else if (c == ')' && depth > 0) depth--;
            else if (depth == 0) sb.append(c);
        }
        return sb.toString();
    }
}*/

public class Kata {
    private static String regex = "\\([^()]*\\)";

    public static String removeParentheses(final String str) {
        var updated = str.replaceAll(regex, "");

        if (updated.contains("(")) {
            updated = removeParentheses(updated);
        }
        return updated;
    }
}