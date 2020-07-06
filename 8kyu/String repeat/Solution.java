/*
Write a function called repeatString which repeats the given String src exactly count times.

        repeatStr(6, "I") // "IIIIII"
        repeatStr(5, "Hello") // "HelloHelloHelloHelloHello"
*/
/*

public class Solution {
    public static String repeatStr(final int repeat, final String string) {
        String result = "";
        for (int i = 0; i < repeat; i++) {
            result += string;
        }
        return result;
    }
}
*/

public class Solution {
    public static String repeatStr(final int repeat, final String string) {
        return repeat > 0 ? string.repeat(repeat) : "";
    }
}