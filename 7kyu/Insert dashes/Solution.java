/*
Write a function insertDash(num)/InsertDash(int num) that will insert dashes ('-')
between each two odd numbers in num.

For example: if num is 454793 the output should be 4547-9-3.
Don't count zero as an odd number.

Note that the number will always be non-negative (>= 0).
*/

public class Solution {
    public static String insertDash(int num) {
        return String.valueOf(num).replaceAll("[13579](?=[13579])", "$0-");
    }
}