public class Solution {
    public static String solve(String str) {
        int openingIndex = str.indexOf("(");
        int closingIndex = str.lastIndexOf(")");

        if (openingIndex < 0) {
            return str;
        }
        int digitPos = openingIndex - 1;
        String prefix = str.substring(0, digitPos);

        char c = str.charAt(digitPos);
        int times = 1;
        String maybeLetter = "";

        if (Character.isDigit(c)) {
            times = Integer.parseInt(String.valueOf(c));
        } else {
            maybeLetter = String.valueOf(c);
        }
        return prefix + maybeLetter + solve(str.substring(openingIndex + 1, closingIndex)).repeat(times);
    }
}

