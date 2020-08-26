/*
The input is a string str of digits.
Cut the string into chunks (a chunk here is a substring of the initial string) of size sz
(ignore the last chunk if its size is less than sz).

If a chunk represents an integer
such as the sum of the cubes of its digits is divisible by 2,
reverse that chunk;
otherwise rotate it to the left by one position.

Put together these modified chunks and return the result as a string.

If      sz is <= 0 or if str is empty return ""
        sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".

Examples:
        revrot("123456987654", 6) --> "234561876549"
        revrot("123456987653", 6) --> "234561356789"
        revrot("66443875", 4) --> "44668753"
        revrot("66443875", 8) --> "64438756"
        revrot("664438769", 8) --> "67834466"
        revrot("123456779", 8) --> "23456771"
        revrot("", 8) --> ""
        revrot("123456779", 0) --> ""
        revrot("563000655734469485", 4) --> "0365065073456944"
*/

import java.util.stream.IntStream;

public class RevRot {
    public static String revRot(String strng, int sz) {
        if (strng.isEmpty() || sz <= 0 || sz > strng.length()) return "";
        var sb = new StringBuilder();

        for (int i = 0; i <= strng.length() - sz; i += sz) {
            var chunk = new StringBuilder(strng.substring(i, sz + i));
            var sum = IntStream.range(0, sz).mapToDouble(j -> Math.pow(chunk.charAt(j), 3)).sum();

            if (sum % 2 == 0) sb.append(chunk.reverse());
            else sb.append(chunk.substring(1, sz)).append(chunk.charAt(0));
        }
        return sb.toString();
    }
}