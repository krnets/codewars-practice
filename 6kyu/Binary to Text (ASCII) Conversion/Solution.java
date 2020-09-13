/*
Write a function that takes in a binary string and returns the equivalent decoded text
(the text is ASCII encoded).

Each 8 bits on the binary string represent 1 character on the ASCII table.

The input string will always be a valid binary string.

Characters can be in the range from "00000000" to "11111111" (inclusive)

Note: In the case of an empty binary string your function should return an empty string.
*/


/*
class Solution {
    public static String binaryToText(String binary) {
        var sb = new StringBuilder();

        for (int i = 0; i < binary.length(); i += Byte.SIZE) {
            String slice = binary.substring(i, i + Byte.SIZE);
            int codePoint = Integer.parseInt(slice, 2);
            sb.append(Character.toString(codePoint));
        }
        return sb.toString();
    }
}
*/

import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Solution {
    public static String binaryToText(String binary) {
        return IntStream.iterate(0, i -> i < binary.length(), i -> i + Byte.SIZE)
                .mapToObj(i -> binary.substring(i, i + Byte.SIZE))
                .mapToInt(n -> Integer.parseInt(n, 2))
                .mapToObj(Character::toString)
                .collect(Collectors.joining());
    }
}
