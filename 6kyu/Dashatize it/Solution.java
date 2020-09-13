/*
Given a number, return a string with dash'-'marks before and after each odd integer,
but do not begin or end the string with a dash mark.

Example:

        dashatize(274) -> '2-7-4'
        dashatize(6815) -> '68-1-5'
*/

public class Solution {
    public static String dashatize(int num) {
        String[] arr = String.valueOf(num)
                .substring(num < 0 ? 1 : 0)
                .split("(?=[13579])|(?<=[13579])");

        return String.join("-", arr);
    }
}