/*
You want to create secret messages which can be deciphered by the Decipher this! kata.
Here are the conditions:

        Your message is a string containing space separated words.
        You need to encrypt each word in the message using the following rules:
        The first letter needs to be converted to its ASCII code.
        The second letter needs to be switched with the last letter
        Keepin' it simple: There are no special characters in input.

Examples:

        Kata.encryptThis("Hello") => "72olle"
        Kata.encryptThis("good") => "103doo"
        Kata.encryptThis("hello world") => "104olle 119drlo"
*/

import java.util.Arrays;
import java.util.stream.Collectors;

public class Kata {
    public static String encryptThis(String text) {
        return Arrays.stream(text.split(" "))
                .map(word -> word.replaceAll("(.)(.)(.*)(.)", "$1$4$3$2"))
                .map(word -> word.isEmpty() ? word : word.replaceFirst(".", String.valueOf((int) word.charAt(0))))
                .collect(Collectors.joining(" "));
    }
}

